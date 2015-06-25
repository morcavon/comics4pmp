#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import mainFrame

#import psyco

#psyco.full()
#psyco.profile(0.0)

modules ={'mainFrame': [1, 'Main frame of Application', 'mainFrame.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = mainFrame.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()