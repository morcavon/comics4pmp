# _*_ coding: mbcs _*_
#-----------------------------------------------------------------------------
# Name:        config.py
#
# Author:      Jae Young
# Email:       morcavon@gmail.com
# Homepage:    http://www.morcavon.com
#
# Created:     2008/12/04
# Copyright:   Copyright (c) morcavon. All rights reserved.
# Licence:     Freeware, see license.txt for details(if any :-))
#-----------------------------------------------------------------------------


import cPickle, os

class Config:
    def __init__(self):
        self.sourceDirectory = "원본 폴더 선택"
        self.destDirectory = "저장 폴더 선택"
        
        self.fileType = "zip"
        
        self.pictureOrder = "right"
        
        self.doCrop = True
        self.doResize = True
        self.resizeSize = 480
        
        self.doZip = True
        self.doZipSplit = False
        self.zipSplitSize = 100
        
        self.doRename = False
        
        self.version = ""
        
    
    @staticmethod
    def getConfig(version):
        retValue = None
        try:
            if not os.path.exists(os.getcwd() + "/config.dat"):
                retValue = Config()
                retValue.version = version
            else:
                retValue = cPickle.load(open(os.getcwd() + "/config.dat", "rb"))
                
                # 기존 config.dat 파일이 현재 프로그램이 사용하는것과 같은지 검사
                print "Config.getConfig.version = ", version, retValue.version
                if retValue.version != version:
                    retValue = Config()
                    retValue.version = version
            
            return retValue
        
        except:
            retValue = Config()
            retValue.version = version
            return retValue
        
        
        
    @staticmethod
    def saveConfig(config):
        cPickle.dump(config, open(os.getcwd() + "/config.dat", "wb"), cPickle.HIGHEST_PROTOCOL)
    
    
    
    
    
    
    
    