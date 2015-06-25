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

        self.recentWorkingDirectory = ""        # zip�� ����ؼ� ��ȯ�ϴ� ��� ���߿� �ٽ� �����Ϸ��� ��ȯ�� ������ ��� �����ߴ��� �����ؾ���.
        

        self.totalFileCount = 0
        self.proceedFileCount = 0
        


    def run(self):

        self.parent.outputText.SetValue("")
        self.parent.mainStatusbar.SetLabel("���� �ð��� ����մϴ�....")
        self.parent.remainTimeGuage.SetValue(0)

        ########################################################################
        
        # ��ȯ�� ��ü ������ ���ϱ�
        
        self.totalFileCount = self.calcTotalSize(self.config.sourceDirectory, "jpg" if self.config.fileType == "jpg" else "zip")
        self.proceedFileCount = 0
        
        if self.config.doZip:
            self.totalFileCount *= 2         # �ٽ� �����ؾ� �ϹǷ� ��Ż ó���ؾ� �� ����Ʈ�� ������ �ι谡 ��
            
        # timer thread ����
        RemainTimer(self).start()
        
        
        
        # conversion....
        self.parent.outputText.AppendText("��ȯ�� �����մϴ�....\n\n")

        for root, dlist, flist in os.walk(self.config.sourceDirectory):

            self.parent.debugOutputText.AppendText("source " + root + "\n")

            if self.config.fileType == "jpg":
                self.pictureCount = 0


            # ���� �ϳ��� �ִ� ���ϵ� ó��
            for fname in filter(lambda x: os.path.splitext(x)[1].lower() == "." + self.config.fileType, flist):      # file type�� �´� ���ϸ� ���
                if not self.convert(os.path.join(root, fname)):
                    return


                ########################################################################
                # compressing....
                if self.config.fileType == "zip":     # zip ������ �����̸�, ���� ���� �ϳ� Ǯ� �� ��ȯ�ѵ�, �ٷ� ����
                    
                    # zip ���� ���ο� ���� Ʈ���� �ִ� ��츦 ����ؾ� �ϹǷ� ������ ����...
                    subDirCount = 0
                    self.compressOneFolder(self.recentWorkingDirectory, fname)
                    
                    self.pictureCount = 0
                ########################################################################


            ########################################################################
            # compressing....                                            # jpg�� �����̸�, ���� �ϳ��� �� ��ȯ�ѵ� ������
            if self.config.fileType == "jpg":
                self.compressOneFolder(root)
            ########################################################################




        # ����.....
        
        self.parent.isRunning = False
        self.parent.buttonEnabling()

        self.parent.outputText.AppendText("\n\n��� �۾��� ���ƽ��ϴ�.\n\n")

        self.finalizing()



    def getPrefix(self, dirName):
        # dir���� source directory�� �� �������� ����
        return dirName.split(self.config.sourceDirectory)[1]



    def washing(self):
        # ��ȯ�� ���� �����̳� ������ ���� (zip ���� �ɼ��� üũ�� ��쿡��)

        if self.config.fileType == "jpg":
            pass
        else:
            pass


    def convert(self, srcFilePath):
        # srcFile -> destFile�� ��ȯ....
        
        if not self.checkThreadState():
            return False

        srcfname = fname = os.path.split(srcFilePath)[1]
        pathSuffix = os.path.split(srcFilePath)[0].split(self.config.sourceDirectory)[1]
        
        destFilePath = self.config.destDirectory + pathSuffix

        if self.config.fileType == "jpg":
            ########################################################################
            # jpg converting
            ########################################################################

            # Ÿ�� ���丮 �˻��ؼ� ������ ����
            if not os.path.exists(destFilePath):
                os.makedirs(destFilePath)

            convertedImage = self.convertOnePicture(srcFilePath)
            for newFileName, img in convertedImage.items():
                newPath = os.path.join(destFilePath, newFileName)
                img.save(newPath, img.format)
                
                self.proceedFileCount += 1
                


        else:
            ########################################################################
            # zip converting, �ϳ��� ���� Ǯ�鼭 �ٷ� �ٷ� ��ȯ ��Ŵ....
            ########################################################################
            self.parent.outputText.AppendText("\n[%s ���� ��ȯ��....]\n" % os.path.split(srcFilePath)[1])

            destFilePath = "%s\\%s" % (destFilePath, os.path.splitext(srcfname)[0])

            if not zipfile.is_zipfile(srcFilePath):
                self.parent.outputText.AppendText("%s: �������� zip ������ �ƴϰų�, �������� �ʴ� ������ �����Դϴ�. ���� ���Ϸ� �Ѿ�ϴ�.\n" % srcFilePath)
            else:
                inZipFile = zipfile.PyZipFile(srcFilePath)
                inZipFile.namelist().sort()
                prevZipDirName = ""
                
                
                
                # zip file ����Ʈ ����
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

                    if os.path.splitext(fname)[1].lower() in (".jpg", ".jpeg"):                  # zip ���ϳ� jpg ���ϸ� ó���ҰŻ�...
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
                        

                        if convertedImage != {}:         # ��ȯ�� �̹����� �ϳ��� �������...
                            # Ÿ�� ���丮 �˻��ؼ� ������ ����

                            if not os.path.exists(targetDir):
                                os.makedirs(targetDir)

                            for newFileName, img in convertedImage.items():
                                newPath = os.path.join(self.recentWorkingDirectory, newFileName).replace("/","\\")
                                if self.parent.enableDebug:
                                    print "convert: newFileName=%s, newPath=%s" % (newFileName, newPath)
                                img.save(newPath, img.format)
                                
                                self.proceedFileCount += 1
                                

                inZipFile.close()
                self.parent.outputText.AppendText("...�Ϸ�\n")


        return True

  


    def convertOnePicture(self, srcFilePath, realFileName = None):
        fname = os.path.split(srcFilePath)[1].lower()
        realFileName = realFileName.lower() if realFileName != None else None
        
        if self.parent.enableDebug:
            print "convertOnePicture: srcFilePath=%s, realFname=%s" % (srcFilePath, realFileName)

        inPic = None
        box = None


        # �̹��� �о����...����ó��
        try:
            self.parent.outputText.AppendText("%s --->" % (fname.strip(".tmp") if realFileName == None else realFileName))

            inPic = Image.open(srcFilePath, "r")
            box = inPic.getbbox()

        except Exception, msg:
            self.parent.debugOutputText.AppendText("%s:%s\nImage open error\n" % (srcFilePath, msg))
            self.parent.outputText.AppendText(" ��ȯ  ����\n")
            return {}

        boxes = []

        # crop ���� üũ
        boxes = [box, ]
        if self.config.doCrop and box[2] >= box[3]:     # ���ΰ� ���κ��� ��� ũ��
            boxes = [(0,0, box[2]/2, box[3]), (box[2]/2, 0, box[2], box[3])]
            self.totalFileCount += 1
          
            

        # �׸� ���� üũ
        if self.config.pictureOrder == "right":
            boxes.reverse()

        # resize
        convertedImages = {}        # ũ�ӵ� ��� �ΰ��� �ǰ���???
        for idx, b in enumerate(boxes):


            # ���� �̸� ���ϱ�....
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
            
            temp.format = inPic.format              # ������ ���� �����͸� �����ؾ���....
            convertedImages[newFileName] = temp

        return convertedImages



    def compressOneFolder(self, zipSourceFileRoot, zipSourceFileName = ""):
        # �ϳ��� ����(zipSourceFileRoot)�� �����Ͽ� �� ���� ������ ����
        
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



        # ��ȯ�� ������ ���°��....
        if not os.path.exists(targetDir):
            self.parent.debugOutputText.AppendText("\n��ȯ�� ���� ����\n")
            return


        # ��ȯ�� ���� ����Ʈ (full path)
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

        self.parent.outputText.AppendText("\n%s ������ ������....." % os.path.split(zipFileFullPath)[1])



        for fpath in filePathList:
            
            fname = os.path.split(fpath)[1]
##            fullPath = os.path.join(targetDir, fname)
            fullPath = fpath
            
            if self.parent.enableDebug: print "compress one folder: fname=%s, fullpath=%s" % (fname, fullPath)

            # ���� ���� üũ
            if self.config.doZipSplit and os.path.getsize(zipFileFullPath) > 0 and os.path.getsize(zipFileFullPath) + os.path.getsize(fullPath) > self.config.zipSplitSize * 1024 * 1024:
                self.parent.outputText.AppendText("\n���� ������ �����մϴ�....")
                outZipFile.close()
                if zipPartNumber == 1:      # 1�� ��Ʈ ���� �̸� ����
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

        # �۾� ���丮 ����
        
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

        self.parent.outputText.AppendText("�Ϸ�\n")




    def checkThreadState(self):
        # ���� ���¸� üũ�Ͽ� stop �̸� False ����
        if self.parent.isRunning:
            return True
        else:
##            self.parent.outputText.AppendText("\n\n����ڿ� ���� �۾��� �ߴ� �Ǿ����ϴ�.\n")
            self.finalizing()
            return False



    def finalizing(self):
        self.parent.isRunning = False
        
        try:

            # �ӽ� ���� ����
            for root, dlist, flist in os.walk(os.getcwd()):
                for fname in filter(lambda x: x.endswith(".tmp"), flist):
                    try:
                        os.remove(os.path.join(root, fname))
                    except:
                        pass
    ##                print fname


##            # Ÿ�� ���丮 ���� (����� zip ������ ��츸)
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
        # dir���� Ȯ���� ext�� �ش��ϴ� ���� ������ ����, zip�� ��� ����� ���� ������ ���ؾ���
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
                            # zip ���Ͽ� ���� ������ �ִ� ��� ī��Ʈ ��������
                            pass

                        totalSize += len(infile.namelist())
                        infile.close()
            
        return totalSize
            
            
            
if __name__ == "__main__":
    print MainThread.calcTotalSize("""D:/MyDoc/photo""", "zip")
        








