# _*_ coding: mbcs _*_
#-----------------------------------------------------------------------------
# Name:        timerThread.py
# Author:      morcavon
# Email:       morcavon@gmail.com
# Homepage:    http://www.morcavon.com
# Created:     2009/03/01
# Copyright:   Copyright (c) morcavon. All rights reserved.
# Licence:     Freeware, see license.txt for details(if any :-))
#-----------------------------------------------------------------------------


from threading import Thread
import time

class RemainTimer(Thread):
    def __init__(self, parent):
        Thread.__init__(self)
        
        self.parent = parent
        self.proceedFileCount = -1      # div 0 error ������
        
        
    def run(self):
        while (self.parent.checkThreadState()):
            # 1�� ���� ���� �ð��� �������� ������
            totalFiles = self.parent.totalFileCount + 1         # div 0 exception ���� ���� 1�� ����....
            proceedFiles = self.parent.proceedFileCount
            remainedFiles = totalFiles - proceedFiles
            filesPerSecond = proceedFiles - self.proceedFileCount
            self.proceedFileCount = proceedFiles

            remainSeconds = 0
            try:
                remainSeconds = (remainedFiles / filesPerSecond)
            except:
                pass
            
##            if self.parent.parent.enableDebug:
##                print "Total files    = %d" % totalFiles
##                print "Proceed files  = %d" % proceedFiles
##                print "Remained files = %d" % remainedFiles
##                print "Remained time  = %d" % remainSeconds
##                print "Files per se   = %d\n" % filesPerSecond

            self.parent.parent.mainStatusbar.SetLabel("���� ���� �ð�...%02d:%02d:%02d" % (remainSeconds / 3600, remainSeconds / 60, remainSeconds % 60))
            self.parent.parent.remainTimeGuage.SetValue(100 - ((remainedFiles * 100.0) / totalFiles))
            
            time.sleep(1.0)
            
            
        self.parent.parent.mainStatusbar.SetLabel("�����")
            
            
            
            
            
            
            
            
            
            
            
