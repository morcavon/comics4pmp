# _*_ coding: mbcs _*_
#-----------------------------------------------------------------------------
# Name:        mainThread.py
#
# Author:      Jae Young
# Email:       morcavon@gmail.com
# Homepage:    http://www.morcavon.com
#
# Created:     2008/12/05
# Version:     0.1.1
# Copyright:   Copyright (c) morcavon. All rights reserved.
# Licence:     Freeware, see license.txt for details(if any :-))
#-----------------------------------------------------------------------------

import os
from threading import Thread
from PIL import Image
from shutil import copy
from shutil import rmtree
import zipfile
from config import Config
from timerThread import RemainTimer


#import psyco
#psyco.full()
#psyco.profile(0.0)


class MainThread(Thread):
    def __init__(self, parent):
        Thread.__init__(self)
        self.parent = parent
        self.config = parent.configuration

        self.pictureCount = 0

        self.recentWorkingDirectory = ""        # zip을 사용해서 변환하는 경우 나중에 다시 압축하려면 변환된 파일을 어디에 저장했는지 추적해야함.
        

        self.totalFileCount = 0
        self.proceedFileCount = 0
        


    def run(self):

        self.parent.outputText.SetValue("")
        self.parent.mainStatusbar.SetLabel("남은 시간을 계산합니다....")
        self.parent.remainTimeGuage.SetValue(0)

        ########################################################################
        
        # 변환할 전체 사이즈 구하기
        
        self.totalFileCount = self.calcTotalSize(self.config.sourceDirectory, "jpg" if self.config.fileType == "jpg" else "zip")
        self.proceedFileCount = 0
        
        if self.config.doZip:
            self.totalFileCount *= 2         # 다시 압축해야 하므로 토탈 처리해야 할 바이트는 원본의 두배가 됨
            
        # timer thread 시작
        RemainTimer(self).start()
        
        
        
        # conversion....
        self.parent.outputText.AppendText("변환을 시작합니다....\n\n")

        for root, dlist, flist in os.walk(self.config.sourceDirectory):

            self.parent.debugOutputText.AppendText("source " + root + "\n")

            if self.config.fileType == "jpg":
                self.pictureCount = 0


            # 폴더 하나에 있는 파일들 처리
            for fname in filter(lambda x: os.path.splitext(x)[1].lower() == "." + self.config.fileType, flist):      # file type에 맞는 파일만 골라냄
                if not self.convert(os.path.join(root, fname)):
                    return


                ########################################################################
                # compressing....
                if self.config.fileType == "zip":     # zip 파일이 원본이면, 압축 파일 하나 풀어서 다 변환한뒤, 바로 압축
                    
                    # zip 파일 내부에 폴더 트리가 있는 경우를 고려해야 하므로 루프를 돌림...
                    subDirCount = 0
                    self.compressOneFolder(self.recentWorkingDirectory, fname)
                    
                    self.pictureCount = 0
                ########################################################################


            ########################################################################
            # compressing....                                            # jpg가 원본이면, 폴더 하나를 다 변환한뒤 압축함
            if self.config.fileType == "jpg":
                self.compressOneFolder(root)
            ########################################################################




        # 종료.....
        
        self.parent.isRunning = False
        self.parent.buttonEnabling()

        self.parent.outputText.AppendText("\n\n모든 작업을 마쳤습니다.\n\n")

        self.finalizing()



    def getPrefix(self, dirName):
        # dir에서 source directory를 뺀 나머지를 리턴
        return dirName.split(self.config.sourceDirectory)[1]



    def washing(self):
        # 변환이 끝난 파일이나 폴더를 정리 (zip 압축 옵션이 체크된 경우에만)

        if self.config.fileType == "jpg":
            pass
        else:
            pass


    def convert(self, srcFilePath):
        # srcFile -> destFile로 변환....
        
        if not self.checkThreadState():
            return False

        srcfname = fname = os.path.split(srcFilePath)[1]
        pathSuffix = os.path.split(srcFilePath)[0].split(self.config.sourceDirectory)[1]
        
        destFilePath = self.config.destDirectory + pathSuffix

        if self.config.fileType == "jpg":
            ########################################################################
            # jpg converting
            ########################################################################

            # 타켓 디렉토리 검사해서 없으면 생성
            if not os.path.exists(destFilePath):
                os.makedirs(destFilePath)

            convertedImage = self.convertOnePicture(srcFilePath)
            for newFileName, img in convertedImage.items():
                newPath = os.path.join(destFilePath, newFileName)
                img.save(newPath, img.format)
                
                self.proceedFileCount += 1
                


        else:
            ########################################################################
            # zip converting, 하나씩 압축 풀면서 바로 바로 변환 시킴....
            ########################################################################
            self.parent.outputText.AppendText("\n[%s 파일 변환중....]\n" % os.path.split(srcFilePath)[1])

            destFilePath = "%s\\%s" % (destFilePath, os.path.splitext(srcfname)[0])

            if not zipfile.is_zipfile(srcFilePath):
                self.parent.outputText.AppendText("%s: 정상적인 zip 파일이 아니거나, 지원되지 않는 형식의 파일입니다. 다음 파일로 넘어갑니다.\n" % srcFilePath)
            else:
                inZipFile = zipfile.PyZipFile(srcFilePath)
                inZipFile.namelist().sort()
                prevZipDirName = ""
                
                
                
                # zip file 리스트 정렬
                sortedList = inZipFile.namelist()
                try:
                    sortedList.sort()
                except:
                    pass
                
                
                for el in sortedList:
                    print el
                
                
                
                
                for fname in sortedList:

                    if not self.checkThreadState():
                        return False

                    tempName = "x.tmp"

                    if os.path.splitext(fname)[1].lower() in (".jpg", ".jpeg"):                  # zip 파일내 jpg 파일만 처리할거삼...
                        open(tempName, "wb").write(inZipFile.read(fname))
                        
                        if self.parent.enableDebug:
                            print "convert: zipped file name=%s" % fname
                            print "convernt: destFilePath=%s" % fname


                        
                        self.recentWorkingDirectory = os.path.join(self.config.destDirectory + pathSuffix, os.path.splitext(srcfname)[0])
                        targetDir = os.path.split(os.path.join(self.recentWorkingDirectory, fname))[0].replace("/","\\")

                        if self.parent.enableDebug: 
                            print "convert: recent w d = ", self.recentWorkingDirectory
                            print "destDir=%s, pathSuffix=%s, tail=%s" % (self.config.destDirectory, pathSuffix, os.path.splitext(srcfname)[0])
                        
                        
                        # ###############################
                        if prevZipDirName != os.path.split(fname)[0]:
                            self.pictureCount = 0
                        convertedImage = self.convertOnePicture(os.path.join(os.getcwd(), tempName), fname)
                        prevZipDirName = os.path.split(fname)[0]
                        # ###############################
                        

                        if convertedImage != {}:         # 변환할 이미지가 하나라도 있을경우...
                            # 타켓 디렉토리 검사해서 없으면 생성

                            if not os.path.exists(targetDir):
                                os.makedirs(targetDir)

                            for newFileName, img in convertedImage.items():
                                newPath = os.path.join(self.recentWorkingDirectory, newFileName).replace("/","\\")
                                if self.parent.enableDebug:
                                    print "convert: newFileName=%s, newPath=%s" % (newFileName, newPath)
                                img.save(newPath, img.format)
                                
                                self.proceedFileCount += 1
                                

                inZipFile.close()
                self.parent.outputText.AppendText("...완료\n")


        return True

  


    def convertOnePicture(self, srcFilePath, realFileName = None):
        fname = os.path.split(srcFilePath)[1].lower()
        realFileName = realFileName.lower() if realFileName != None else None
        
        if self.parent.enableDebug:
            print "convertOnePicture: srcFilePath=%s, realFname=%s" % (srcFilePath, realFileName)

        inPic = None
        box = None


        # 이미지 읽어오기...예외처리
        try:
            self.parent.outputText.AppendText("%s --->" % (fname.strip(".tmp") if realFileName == None else realFileName))

            inPic = Image.open(srcFilePath, "r")
            box = inPic.getbbox()

        except Exception, msg:
            self.parent.debugOutputText.AppendText("%s:%s\nImage open error\n" % (srcFilePath, msg))
            self.parent.outputText.AppendText(" 변환  오류\n")
            return {}

        boxes = []

        # crop 여부 체크
        boxes = [box, ]
        if self.config.doCrop and box[2] >= box[3]:     # 가로가 세로보다 길면 크롭
            boxes = [(0,0, box[2]/2, box[3]), (box[2]/2, 0, box[2], box[3])]
            self.totalFileCount += 1
          
            

        # 그림 순서 체크
        if self.config.pictureOrder == "right":
            boxes.reverse()

        # resize
        convertedImages = {}        # 크롭된 경우 두개가 되겠지???
        for idx, b in enumerate(boxes):


            # 파일 이름 정하기....
            if self.config.doRename:
                newFileName = "%010d.jpg" % self.pictureCount
                self.pictureCount = self.pictureCount + 1
                
            else:
                newFileName = "%s_%s.jpg" % (fname.strip(".tmp").strip(".jpg") if realFileName == None else os.path.split(realFileName)[1].strip(".jpg"), "a" if idx == 0 else "b")
                
            if realFileName != None:
                    newFileName = os.path.split(realFileName)[0] + "\\" + newFileName
                
            

            newFileName = newFileName.replace("/","\\").strip("\\")


            self.parent.outputText.AppendText(" %s\n" % (newFileName))

            temp = inPic.crop(b) if self.config.doCrop else inPic
            if self.config.doResize and (b[2] - b[0] > self.config.resizeSize):
                temp = temp.resize((self.config.resizeSize, int(float(self.config.resizeSize)*temp.size[1]/temp.size[0])), resample=3)
            
            temp.format = inPic.format              # 원본의 포맷 데이터를 유지해야함....
            convertedImages[newFileName] = temp

        return convertedImages



    def compressOneFolder(self, zipSourceFileRoot, zipSourceFileName = ""):
        # 하나의 폴더(zipSourceFileRoot)를 압축하여 그 상위 폴더에 생성
        
##        if self.parent.enableDebug: print "compressOneFolder: root= %s, name=%s" % (zipSourceFileRoot, zipSourceFileName)

        if not self.config.doZip:
            return


        self.parent.debugOutputText.AppendText("\nroot=%s\nname=%s\n" % (zipSourceFileRoot, zipSourceFileName))

        pathSuffix = ""
        try:
            pathSuffix = zipSourceFileRoot.split(self.config.destDirectory if self.config.fileType == "zip" else self.config.sourceDirectory)[1]
        except:
            pass

        targetDir = os.path.join(self.config.destDirectory, pathSuffix.strip("\\")).strip("\\")

        self.parent.debugOutputText.AppendText("\ntargetDIR = %s\n" % targetDir)



        # 변환된 파일이 없는경우....
        if not os.path.exists(targetDir):
            self.parent.debugOutputText.AppendText("\n변환된 파일 없음\n")
            return


        # 변환할 파일 리스트 (full path)
        dirListSet = set([targetDir])
        filePathList = []
        for root, dlist, flist in os.walk(targetDir):
            
            for fname in filter(lambda x: os.path.splitext(x)[1].lower() in (".jpg", ".jpeg"), flist):
                fpath = os.path.join(root, fname)
                filePathList.append(fpath)
                dirListSet.add(os.path.split(fpath)[0])



        if not len(filePathList) > 1:
            return



        zipFileFullPath = os.path.join(self.config.destDirectory,
                                       ("%s_%s%scomics4PMP.zip" % ('_'.join(pathSuffix.split("\\")).strip("_") if pathSuffix != "" else os.path.split(self.config.destDirectory)[1],
#                                                                    "_" if pathSuffix != "" else "",
                                                                    "", "")))
##                                                                    zipSourceFileName[:-4], "_" if zipSourceFileName[:-4] != "" else "")))
        outZipFile = zipfile.ZipFile(zipFileFullPath, "w", zipfile.ZIP_DEFLATED)



        self.parent.debugOutputText.AppendText("targetDir=%s\ndest=%s\nsuffix=%s\n\n" % (targetDir, self.config.destDirectory, pathSuffix))
        self.parent.debugOutputText.AppendText("\noutzipfile=%s" % zipFileFullPath)



        zipPartNumber = 1
        isDone = False

        self.parent.outputText.AppendText("\n%s 파일을 생성중....." % os.path.split(zipFileFullPath)[1])



        for fpath in filePathList:
            
            fname = os.path.split(fpath)[1]
##            fullPath = os.path.join(targetDir, fname)
            fullPath = fpath
            
            if self.parent.enableDebug: print "compress one folder: fname=%s, fullpath=%s" % (fname, fullPath)

            # 분할 압축 체크
            if self.config.doZipSplit and os.path.getsize(zipFileFullPath) > 0 and os.path.getsize(zipFileFullPath) + os.path.getsize(fullPath) > self.config.zipSplitSize * 1024 * 1024:
                self.parent.outputText.AppendText("\n압축 파일을 분할합니다....")
                outZipFile.close()
                if zipPartNumber == 1:      # 1번 파트 파일 이름 변경
                    newPartName = zipFileFullPath.replace("comics4PMP",
                                                "comics4PMP_part%02d" % zipPartNumber)
                    if os.path.exists(newPartName):
                        os.remove(newPartName)
                    os.rename(zipFileFullPath, newPartName)

                zipPartNumber += 1
                zipFileFullPath = os.path.join(self.config.destDirectory,
                                       ("%s_%s%scomics4PMP_part%02d.zip" % ('_'.join(pathSuffix.split("\\")).strip("_") if pathSuffix != "" else os.path.split(self.config.destDirectory)[1],
##                                                                    zipSourceFileName[:-4], "_" if zipSourceFileName[:-4] != "" else "", zipPartNumber)))
                                                                      "", "", zipPartNumber)))
                outZipFile = zipfile.ZipFile(zipFileFullPath, "w", zipfile.ZIP_DEFLATED)
                self.parent.outputText.AppendText("%s\n" % os.path.split(zipFileFullPath)[1])

            outZipFile.write(fullPath, arcname=fullPath.split(targetDir)[1], compress_type=zipfile.ZIP_DEFLATED)
            
            self.proceedFileCount += 1

            os.remove(fpath)

        # 작업 디렉토리 비우기
        
        for dirNameToRemove in dirListSet:
            
            if dirNameToRemove != self.config.destDirectory:
                try:
                    rmtree(dirNameToRemove)
                    if self.parent.enableDebug: print "dir to remove: ", dirNameToRemove
                except:
                    pass
                
                

        isDone = True



##        if targetDir != self.config.destDirectory:
##            try:
##                rmtree(targetDir)
##            except Exception, msg:
##                if self.parent.enableDebug: print "Exception from compressOneFolder:\n", msg

        self.parent.outputText.AppendText("완료\n")




    def checkThreadState(self):
        # 현재 상태를 체크하여 stop 이면 False 리턴
        if self.parent.isRunning:
            return True
        else:
##            self.parent.outputText.AppendText("\n\n사용자에 의해 작업이 중단 되었습니다.\n")
            self.finalizing()
            return False



    def finalizing(self):
        self.parent.isRunning = False
        
        try:

            # 임시 파일 지움
            for root, dlist, flist in os.walk(os.getcwd()):
                for fname in filter(lambda x: x.endswith(".tmp"), flist):
                    try:
                        os.remove(os.path.join(root, fname))
                    except:
                        pass
    ##                print fname


##            # 타겟 디렉토리 정리 (결과를 zip 압축한 경우만)
##            if self.config.doZip:
##                if self.parent.enableDebug: print "finalizing:target dir cleaning..."
##                for root, dlist, flist in os.walk(self.config.destDirectory):
##                    for dname in dlist:
##                        rmtree(os.path.join(root, dname))
        
        except:
            pass
        
        

        self.parent.debugOutputText.AppendText("\n%d %d\n" % (self.totalFileCount, self.proceedFileCount))

        return
    
    
    
    @staticmethod
    def calcTotalSize(dir, ext):
        # dir에서 확장자 ext에 해당하는 파일 갯수를 구함, zip인 경우 압축된 파일 개수를 구해야함
        totalSize = 0
        
        for root, dlist, flist in os.walk(dir):
            for fname in flist:
                if fname[-3:].lower() == ext:
                    if ext == "jpg":
                        totalSize += 1
                    else:
                        infile = None
                        
                        try:
                            infile = zipfile.PyZipFile(os.path.join(root, fname))
                        except:
                            # zip 파일에 뭔가 문제가 있는 경우 카운트 하지않음
                            pass

                        totalSize += len(infile.namelist())
                        infile.close()
            
        return totalSize
            
            
            
if __name__ == "__main__":
    print MainThread.calcTotalSize("""D:/MyDoc/photo""", "zip")
        








