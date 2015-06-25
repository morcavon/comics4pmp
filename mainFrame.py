# _*_ coding: mbcs _*_
#-----------------------------------------------------------------------------
# Name:        mainFrame.py
#
# Author:      Jae Young
# Email:       morcavon@gmail.com
# Homepage:    http://www.morcavon.com
# PERM LINK:   http://www.morcavon.com/1178440429 / 원래는 979
# Created:     2008/12/04
# Version:     0.2.82
# Copyright:   Copyright (c) morcavon. All rights reserved.
# Licence:     Freeware, see license.txt for details(if any :-))
#-----------------------------------------------------------------------------
#Boa:Frame:Frame1


version = "0.2.82"


import wx
from wx.lib.anchors import LayoutAnchors

import icon

import os, urllib, re, time
from about import About
from config import Config
from mainThread import MainThread
import shutil


#import psyco
#psyco.full()
#psyco.profile(0.0)



def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON3, wxID_FRAME1BUTTON4, wxID_FRAME1BUTTON5, 
 wxID_FRAME1BUTTON6, wxID_FRAME1DEBUGOUTPUTTEXT, wxID_FRAME1DORENAMECHECKBOX, 
 wxID_FRAME1ENABLECROPCHECKBOX, wxID_FRAME1ENABLELONGSIDESIZECHECKBOX, 
 wxID_FRAME1ENABLESPLITCHECKBOX, wxID_FRAME1ENABLEZIPCOMPRESSCHECKBOX, 
 wxID_FRAME1JPGRADIOBUTTON, wxID_FRAME1LONGSIDESIZECOMBOBOX, 
 wxID_FRAME1MAINSTATUSBAR, wxID_FRAME1OUTPUTTEXT, 
 wxID_FRAME1PICTUREORDERLEFTFIRSTRADIOBUTTON, 
 wxID_FRAME1PICTUREORDERRIGHTFIRSTRADIOBUTTON, wxID_FRAME1REMAINTIMEGUAGE, 
 wxID_FRAME1SELECTDESTBUTTON, wxID_FRAME1SELECTSRCBUTTON, 
 wxID_FRAME1SPLITSIZECOMBOBOX, wxID_FRAME1STARTBUTTON, wxID_FRAME1STATICBOX1, 
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, wxID_FRAME1STOPBUTTON, 
 wxID_FRAME1ZIPRADIOBUTTON, 
] = [wx.NewId() for _init_ctrls in range(27)]

[wxID_FRAME1ABOUTMENUABOUTMENUWHOITEM] = [wx.NewId() for _init_coll_aboutMenu_Items in range(1)]

class Frame1(wx.Frame):
    def _init_coll_aboutMenu_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_FRAME1ABOUTMENUABOUTMENUWHOITEM,
              kind=wx.ITEM_NORMAL, text='\xb8\xb8\xb5\xe7\xc0\xcc')
        self.Bind(wx.EVT_MENU, self.OnAboutMenuAboutmenuwhoitemMenu,
              id=wxID_FRAME1ABOUTMENUABOUTMENUWHOITEM)

    def _init_coll_menuBar1_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.aboutMenu, title='About')

    def _init_utils(self):
        # generated method, don't edit
        self.menuBar1 = wx.MenuBar()
        self.menuBar1.SetBackgroundColour(wx.Colour(191, 214, 232))
        self.menuBar1.SetBackgroundStyle(2)

        self.aboutMenu = wx.Menu(title='')

        self._init_coll_menuBar1_Menus(self.menuBar1)
        self._init_coll_aboutMenu_Items(self.aboutMenu)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(544, 242), size=wx.Size(839, 526),
              style=~wx.MAXIMIZE_BOX & ~wx.MAXIMIZE & ~wx.RESIZE_BORDER & wx.DEFAULT_FRAME_STYLE,
              title='comics4PMP')
        self._init_utils()
        self.SetClientSize(wx.Size(831, 499))
        self.SetMenuBar(self.menuBar1)
        self.SetBackgroundColour(wx.Colour(220, 233, 235))
        self.SetToolTipString('')
        self.SetThemeEnabled(False)
        self.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.Bind(wx.EVT_CLOSE, self.OnFrame1Close)
        self.Bind(wx.EVT_DROP_FILES, self.OnFrame1DropFiles)

        self.outputText = wx.TextCtrl(id=wxID_FRAME1OUTPUTTEXT,
              name='outputText', parent=self, pos=wx.Point(400, 72),
              size=wx.Size(429, 384),
              style=wx.TE_MULTILINE | wx.VSCROLL | wx.TE_READONLY,
              value='"JPG4PSP"\xc0\xc7 \xbe\xf7\xb1\xd7\xb7\xb9\xc0\xcc\xb5\xe5 \xb9\xf6\xc0\xfc\xc0\xd4\xb4\xcf\xb4\xd9.\n\n\xc0\xce\xc5\xcd\xc6\xe4\xc0\xcc\xbd\xba\xb4\xc2 \xb0\xa1\xb4\xc9\xc7\xd1 \xb0\xa3\xb4\xdc\xc7\xcf\xb0\xd4 \xb8\xb8\xb5\xe9\xb7\xc1\xb0\xed \xc7\xdf\xc0\xb8\xb4\xcf \xbb\xe7\xbf\xeb\xc7\xcf\xbd\xc3\xb4\xc2\xb5\xa5\xbf\xa1 \xbe\xee\xb7\xc1\xbf\xf2\xc0\xbb \xbe\xf8\xc0\xbb\xb0\xc5\xb6\xf3 \xbb\xfd\xb0\xa2\xc7\xd5\xb4\xcf\xb4\xd9~\n\n\n1. \xba\xaf\xc8\xaf\xc7\xd2 \xc6\xc4\xc0\xcf(jpg \xc8\xa4\xc0\xba zip)\xc0\xcc \xc0\xd6\xb4\xc2 \xc6\xfa\xb4\xf5 \xbc\xb1\xc5\xc3 \n   \xbc\xb1\xc5\xc3\xb5\xc8 \xc6\xfa\xb4\xf5\xbf\xa1 \xc0\xd6\xb4\xc2 \xb8\xf0\xb5\xe7 \xc6\xc4\xc0\xcf\xb0\xfa \xc7\xcf\xc0\xa7 \xc6\xfa\xb4\xf5(\xc7\xcf\xc0\xa7 \xc6\xfa\xb4\xf5\xc0\xc7 \xc7\xcf\xc0\xa7 \xc6\xfa\xb4\xf5\xb4\xc2 \xc0\xdb\xbe\xf7\xc7\xcf\xc1\xf6 \xbe\xca\xc0\xbd)\xb8\xa6 \xba\xaf\xc8\xaf\xc7\xd5\xb4\xcf\xb4\xd9.\n\n2. \xb1\xd7\xb8\xb2 \xc0\xda\xb8\xa3\xb4\xc2 \xbc\xf8\xbc\xad \xbc\xb1\xc5\xc3\n\n3. \xc5\xa9\xb7\xd3 \xbf\xa9\xba\xce \xbc\xb1\xc5\xc3\n   \xb0\xa1\xb7\xce\xb0\xa1 \xbc\xbc\xb7\xce\xba\xb8\xb4\xd9 \xb1\xe4 \xb0\xe6\xbf\xec\xbf\xa1\xb8\xb8 \xb0\xa1\xb7\xce\xb8\xa6 \xb9\xdd\xc0\xb8\xb7\xce \xc0\xda\xb8\xa8\xb4\xcf\xb4\xd9.\n\n4. \xb0\xa1\xb7\xce\xc3\xe0 \xbb\xe7\xc0\xcc\xc1\xee \xc1\xb6\xc0\xfd\n    (\xc5\xa9\xb7\xd3\xc7\xd1 \xb0\xe6\xbf\xec\xbf\xa1\xb4\xc2 \xc5\xa9\xb7\xd3\xb5\xc8 \xb1\xd7\xb8\xb2\xc0\xc7) \xb0\xa1\xb7\xce \xb1\xe6\xc0\xcc\xb8\xa6 \xc1\xb6\xc0\xfd\xc7\xd5\xb4\xcf\xb4\xd9. \xbc\xbc\xb7\xce \xc5\xa9\xb1\xe2\xb5\xb5 \xb1\xd7\xbf\xa1 \xb8\xc2\xb0\xd4 \xc0\xda\xb5\xbf\xc0\xb8\xb7\xce \xc1\xb6\xc0\xfd\xb5\xc7\xb0\xda\xc1\xd2? :-)\n\n5. zip \xbe\xd0\xc3\xe0 \xbf\xa9\xba\xce \xbc\xb1\xc5\xc3\n   \xba\xaf\xc8\xaf\xb5\xc8 jpg \xc6\xc4\xc0\xcf\xc0\xcc \xc0\xfa\xc0\xe5\xb5\xc8 \xc6\xfa\xb4\xf5\xb8\xa6 zip\xc0\xb8\xb7\xce \xbe\xd0\xc3\xe0\xc7\xd5\xb4\xcf\xb4\xd9. \xc6\xfa\xb4\xf5\xba\xb0\xb7\xce \xb0\xa2\xb0\xa2\xc0\xc7 zip \xc6\xc4\xc0\xcf\xc0\xcc \xbb\xfd\xbc\xba\xb5\xcb\xb4\xcf\xb4\xd9.\n\n6. \xba\xd0\xc7\xd2 \xbe\xd0\xc3\xe0 \xc5\xa9\xb1\xe2 \xbc\xb1\xc5\xc3\n   zip\xc0\xb8\xb7\xce \xbe\xd0\xc3\xe0\xc7\xd2\xb6\xa7 \xba\xd0\xc7\xd2 \xbe\xd0\xc3\xe0\xc0\xbb \xc0\xa7\xc7\xd1 \xc5\xa9\xb1\xe2\xb8\xa6 \xbc\xb3\xc1\xa4\xc7\xd5\xb4\xcf\xb4\xd9. \n\n\n\xbb\xe7\xbf\xeb\xc1\xdf\xbf\xa1 \xb1\xc3\xb1\xdd\xc7\xd1\xc1\xa1\xc0\xcc\xb3\xaa \xc0\xc7\xb0\xdf\xc0\xba \xc0\xcc\xb0\xf7\xc0\xb8\xb7\xce \xba\xce\xc5\xb9\xb5\xe5\xb8\xb3\xb4\xcf\xb4\xd9~\n\nhttp://www.morcavon.com/1178440429\n\xc1\xa6\xc0\xdb\xc0\xda: morcavon')
        self.outputText.SetConstraints(LayoutAnchors(self.outputText, True,
              True, False, False))
        self.outputText.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Arial'))

        self.selectDestButton = wx.Button(id=wxID_FRAME1SELECTDESTBUTTON,
              label='\xc0\xfa\xc0\xe5 \xc6\xfa\xb4\xf5 \xbc\xb1\xc5\xc3',
              name='selectDestButton', parent=self, pos=wx.Point(72, 40),
              size=wx.Size(752, 24), style=0)
        self.selectDestButton.SetToolTipString('\xba\xaf\xc8\xaf\xb5\xc8 \xc6\xc4\xc0\xcf\xc0\xcc \xc0\xfa\xc0\xe5\xb5\xc9 \xc6\xfa\xb4\xf5\xb8\xa6 \xbc\xb1\xc5\xc3\xc7\xd5\xb4\xcf\xb4\xd9.\n\xbf\xf8\xba\xbb\xc0\xcc \xbf\xa9\xb7\xaf\xb0\xb3\xc0\xc7 \xc6\xfa\xb4\xf5 \xc8\xa4\xc0\xba zip \xc6\xc4\xc0\xcf\xc0\xce \xb0\xe6\xbf\xec \xb0\xa2\xb0\xa2\xc0\xc7 \xc6\xfa\xb4\xf5\xb8\xa6 \xbb\xfd\xbc\xba\xc7\xcf\xbf\xa9 \xba\xaf\xc8\xaf\xb5\xc8 \xc6\xc4\xc0\xcf\xc0\xbb \xc0\xfa\xc0\xe5\xc7\xd5\xb4\xcf\xb4\xd9.')
        self.selectDestButton.SetBackgroundColour(wx.Colour(213, 249, 249))
        self.selectDestButton.Bind(wx.EVT_BUTTON, self.OnSelectDestButtonButton,
              id=wxID_FRAME1SELECTDESTBUTTON)

        self.selectSrcButton = wx.Button(id=wxID_FRAME1SELECTSRCBUTTON,
              label='\xbf\xf8\xba\xbb \xc6\xfa\xb4\xf5 \xbc\xb1\xc5\xc3',
              name='selectSrcButton', parent=self, pos=wx.Point(72, 8),
              size=wx.Size(752, 24), style=0)
        self.selectSrcButton.SetToolTipString('\xba\xaf\xc8\xaf\xc7\xd2 \xc6\xc4\xc0\xcf(jpg \xc8\xa4\xc0\xba zip)\xc0\xcc \xc0\xd6\xb4\xc2 \xc6\xfa\xb4\xf5\xb8\xa6 \xbc\xb1\xc5\xc3\xc7\xd5\xb4\xcf\xb4\xd9.\n\xbc\xb1\xc5\xc3\xb5\xc8 \xc6\xfa\xb4\xf5\xbf\xcd \xb8\xf0\xb5\xe7 \xc7\xcf\xc0\xa7 \xc6\xfa\xb4\xf5\xbf\xa1 \xb4\xeb\xc7\xd8\xbc\xad \xba\xaf\xc8\xaf \xc0\xdb\xbe\xf7\xc0\xbb \xc7\xcf\xb0\xd4\xb5\xcb\xb4\xcf\xb4\xd9.')
        self.selectSrcButton.SetBackgroundColour(wx.Colour(213, 249, 249))
        self.selectSrcButton.Bind(wx.EVT_BUTTON, self.OnSelectSrcButtonButton,
              id=wxID_FRAME1SELECTSRCBUTTON)

        self.stopButton = wx.Button(id=wxID_FRAME1STOPBUTTON,
              label='\xba\xaf\xc8\xaf \xc1\xdf\xc1\xf6', name='stopButton',
              parent=self, pos=wx.Point(296, 408), size=wx.Size(96, 40),
              style=0)
        self.stopButton.SetBackgroundColour(wx.Colour(250, 184, 193))
        self.stopButton.Bind(wx.EVT_BUTTON, self.OnStopButtonButton,
              id=wxID_FRAME1STOPBUTTON)

        self.startButton = wx.Button(id=wxID_FRAME1STARTBUTTON,
              label='\xba\xaf\xc8\xaf \xbd\xc3\xc0\xdb', name='startButton',
              parent=self, pos=wx.Point(296, 344), size=wx.Size(96, 40),
              style=0)
        self.startButton.SetBackgroundColour(wx.Colour(250, 184, 193))
        self.startButton.Bind(wx.EVT_BUTTON, self.OnStartButtonButton,
              id=wxID_FRAME1STARTBUTTON)

        self.jpgRadioButton = wx.RadioButton(id=wxID_FRAME1JPGRADIOBUTTON,
              label='jpg', name='jpgRadioButton', parent=self, pos=wx.Point(8,
              16), size=wx.Size(56, 14), style=wx.RB_GROUP)
        self.jpgRadioButton.SetValue(True)
        self.jpgRadioButton.SetToolTipString('\xbf\xf8\xba\xbb \xc6\xfa\xb4\xf5\xbf\xa1\xbc\xad \xba\xaf\xc8\xaf\xc7\xcf\xb7\xc1\xb4\xc2 \xc6\xc4\xc0\xcf\xc0\xc7 \xc1\xbe\xb7\xf9\xb8\xa6 \xbc\xb1\xc5\xc3\xc7\xd5\xb4\xcf\xb4\xd9.\njpg, zip \xb5\xd1 \xc1\xdf \xc7\xcf\xb3\xaa\xb8\xb8 \xbc\xb1\xc5\xc3 \xb0\xa1\xb4\xc9\xc7\xd5\xb4\xcf\xb4\xd9.')

        self.zipRadioButton = wx.RadioButton(id=wxID_FRAME1ZIPRADIOBUTTON,
              label='zip', name='zipRadioButton', parent=self, pos=wx.Point(8,
              40), size=wx.Size(56, 14), style=0)
        self.zipRadioButton.SetValue(True)
        self.zipRadioButton.SetToolTipString('\xbf\xf8\xba\xbb \xc6\xfa\xb4\xf5\xbf\xa1\xbc\xad \xba\xaf\xc8\xaf\xc7\xcf\xb7\xc1\xb4\xc2 \xc6\xc4\xc0\xcf\xc0\xc7 \xc1\xbe\xb7\xf9\xb8\xa6 \xbc\xb1\xc5\xc3\xc7\xd5\xb4\xcf\xb4\xd9.\njpg, zip \xb5\xd1 \xc1\xdf \xc7\xcf\xb3\xaa\xb8\xb8 \xbc\xb1\xc5\xc3 \xb0\xa1\xb4\xc9\xc7\xd5\xb4\xcf\xb4\xd9.')

        self.longSideSizeComboBox = wx.ComboBox(choices=["240", "272", "320",
              "480"], id=wxID_FRAME1LONGSIDESIZECOMBOBOX,
              name='longSideSizeComboBox', parent=self, pos=wx.Point(152, 360),
              size=wx.Size(80, 22), style=0, value='480')
        self.longSideSizeComboBox.SetLabel('480')

        self.enableCropCheckBox = wx.CheckBox(id=wxID_FRAME1ENABLECROPCHECKBOX,
              label='\xb1\xd7\xb8\xb2 \xc5\xa9\xb7\xd3',
              name='enableCropCheckBox', parent=self, pos=wx.Point(8, 336),
              size=wx.Size(144, 22), style=0)
        self.enableCropCheckBox.SetValue(True)
        self.enableCropCheckBox.SetToolTipString('\xb1\xd7\xb8\xb2\xc0\xbb \xc5\xa9\xb7\xd3\xc7\xd2\xc1\xf6 \xbf\xa9\xba\xce\xb8\xa6 \xbc\xb1\xc5\xc3\xc7\xd5\xb4\xcf\xb4\xd9.\n\xbc\xb1\xc5\xc3\xc7\xcf\xb8\xe9 \xb1\xd7\xb8\xb2\xc0\xc7 \xb0\xa1\xb7\xce\xb0\xa1 \xbc\xbc\xb7\xce\xba\xb8\xb4\xd9 \xb1\xe4 \xb0\xe6\xbf\xec, \xb0\xa1\xb7\xce\xb8\xa6 \xb9\xdd\xc0\xb8\xb7\xce \xc0\xda\xb8\xa8\xb4\xcf\xb4\xd9.\n(\xbf\xb91: \xb0\xa1\xb7\xce800/\xbc\xbc\xb7\xce500\xc0\xce \xb0\xe6\xbf\xec => \xb0\xa1\xb7\xce400/\xbc\xbc\xb7\xce500 \xb5\xce\xc0\xe5\xc0\xb8\xb7\xce \xc0\xda\xb8\xa8\xb4\xcf\xb4\xd9)\n(\xbf\xb92: \xb0\xa1\xb7\xce800/\xbc\xbc\xb7\xce1000\xc0\xce \xb0\xe6\xbf\xec => \xc0\xda\xb8\xa3\xc1\xf6 \xbe\xca\xb0\xed \xc7\xd1\xc0\xe5\xc0\xb8\xb7\xce \xc3\xb3\xb8\xae\xc7\xd5\xb4\xcf\xb4\xd9)\n')

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='pixel', name='staticText1', parent=self, pos=wx.Point(240,
              368), size=wx.Size(40, 14), style=0)

        self.enableSplitCheckbox = wx.CheckBox(id=wxID_FRAME1ENABLESPLITCHECKBOX,
              label='zip \xc6\xc4\xc0\xcf \xba\xd0\xc7\xd2 \xbe\xd0\xc3\xe0',
              name='enableSplitCheckbox', parent=self, pos=wx.Point(8, 424),
              size=wx.Size(144, 22), style=0)
        self.enableSplitCheckbox.SetValue(True)
        self.enableSplitCheckbox.SetToolTipString('zip \xc6\xc4\xc0\xcf\xc0\xbb \xba\xd0\xc7\xd2 \xbe\xd0\xc3\xe0\xc7\xd2\xc1\xf6 \xbf\xa9\xba\xce\xbf\xcd \xba\xd0\xc7\xd2 \xc5\xa9\xb1\xe2\xb8\xa6 \xbc\xb3\xc1\xa4\xc7\xd5\xb4\xcf\xb4\xd9.\n\xba\xd0\xc7\xd2\xb5\xc8 \xc6\xc4\xc0\xcf\xc0\xba "\xc6\xc4\xc0\xcf\xb8\xed_part1.zip", "\xc6\xc4\xc0\xcf\xb8\xed_part2.zip"...\xc0\xcc\xb7\xb1\xbd\xc4\xc0\xb8\xb7\xce \xbb\xfd\xbc\xba\xb5\xcb\xb4\xcf\xb4\xd9.')

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2, label='MB',
              name='staticText2', parent=self, pos=wx.Point(240, 432),
              size=wx.Size(16, 14), style=0)

        self.splitSizeComboBox = wx.ComboBox(choices=["10", "50", "100", "200"],
              id=wxID_FRAME1SPLITSIZECOMBOBOX, name='splitSizeComboBox',
              parent=self, pos=wx.Point(152, 424), size=wx.Size(80, 22),
              style=0, value='100')
        self.splitSizeComboBox.SetLabel('100')

        self.enableLongSideSizeCheckBox = wx.CheckBox(id=wxID_FRAME1ENABLELONGSIDESIZECHECKBOX,
              label='\xb0\xa1\xb7\xce \xc3\xe0 \xbb\xe7\xc0\xcc\xc1\xee \xc1\xb6\xc0\xfd',
              name='enableLongSideSizeCheckBox', parent=self, pos=wx.Point(8,
              360), size=wx.Size(144, 22), style=0)
        self.enableLongSideSizeCheckBox.SetValue(True)
        self.enableLongSideSizeCheckBox.SetToolTipString('\xb1\xd7\xb8\xb2\xc0\xbb \xba\xaf\xc8\xaf\xc7\xd2\xb6\xa7 \xc5\xa9\xb7\xd3\xb5\xc8 \xb1\xd7\xb8\xb2\xc0\xc7 \xb1\xe4 \xc3\xe0\xc0\xc7 \xbb\xe7\xc0\xcc\xc1\xee \xb8\xa6 \xc1\xb6\xc0\xfd\xc7\xd2\xc1\xf6 \xbf\xa9\xba\xce\xbf\xcd \xc5\xa9\xb1\xe2\xb8\xa6 \xbc\xb3\xc1\xa4\xc7\xd5\xb4\xcf\xb4\xd9.\n\xbb\xe7\xc0\xcc\xc1\xee\xb8\xa6 \xba\xaf\xb0\xe6\xc7\xcf\xb8\xe9 \xb1\xe4 \xc3\xe0\xc0\xc7 \xb1\xe6\xc0\xcc\xbf\xa1 \xb8\xc2\xc3\xdf\xbe\xee \xc2\xaa\xc0\xba \xc3\xe0\xc0\xc7 \xb1\xe6\xc0\xcc\xb5\xb5 \xc0\xda\xb5\xbf\xc0\xb8\xb7\xce \xba\xaf\xb0\xe6\xb5\xcb\xb4\xcf\xb4\xd9.\n(\xc5\xa9\xb7\xd3\xb5\xc8 \xb1\xd7\xb8\xb2\xc0\xc7 \xb1\xe4 \xc3\xe0\xc0\xcc \xbf\xa9\xb1\xe2\xbc\xad \xbc\xb3\xc1\xa4\xb5\xc8 \xb0\xaa\xba\xb8\xb4\xd9 \xc0\xdb\xc0\xbb \xb0\xe6\xbf\xec \xbe\xc6\xb9\xab\xb0\xcd\xb5\xb5 \xbe\xc8\xc7\xd5\xb4\xcf\xb4\xd9)')

        self.enableZipCompressCheckBox = wx.CheckBox(id=wxID_FRAME1ENABLEZIPCOMPRESSCHECKBOX,
              label='zip\xc0\xb8\xb7\xce \xbe\xd0\xc3\xe0',
              name='enableZipCompressCheckBox', parent=self, pos=wx.Point(8,
              400), size=wx.Size(144, 22), style=0)
        self.enableZipCompressCheckBox.SetValue(True)
        self.enableZipCompressCheckBox.SetToolTipString('\xba\xaf\xc8\xaf\xb5\xc8 jpg \xc6\xc4\xc0\xcf\xc0\xbb zip\xc0\xb8\xb7\xce \xbe\xd0\xc3\xe0\xc7\xd2\xc1\xf6 \xbf\xa9\xba\xce\xb8\xa6 \xbc\xb1\xc5\xc3\xc7\xd5\xb4\xcf\xb4\xd9.')

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1,
              label='\xc0\xdf\xb6\xf3\xb3\xbd \xb1\xd7\xb8\xb2\xc0\xc7 \xbc\xf8\xbc\xad',
              name='staticBox1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(0, 0), style=0)

        self.pictureOrderLeftFirstRadioButton = wx.RadioButton(id=wxID_FRAME1PICTUREORDERLEFTFIRSTRADIOBUTTON,
              label='', name='pictureOrderLeftFirstRadioButton', parent=self,
              pos=wx.Point(24, 136), size=wx.Size(16, 14), style=wx.RB_GROUP)
        self.pictureOrderLeftFirstRadioButton.SetValue(True)

        self.pictureOrderRightFirstRadioButton = wx.RadioButton(id=wxID_FRAME1PICTUREORDERRIGHTFIRSTRADIOBUTTON,
              label='', name='pictureOrderRightFirstRadioButton', parent=self,
              pos=wx.Point(24, 240), size=wx.Size(16, 14), style=0)
        self.pictureOrderRightFirstRadioButton.SetValue(True)

        self.button4 = wx.Button(id=wxID_FRAME1BUTTON4, label='2',
              name='button4', parent=self, pos=wx.Point(128, 120),
              size=wx.Size(56, 72), style=wx.NO_BORDER)
        self.button4.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Tahoma'))
        self.button4.Enable(False)
        self.button4.SetBackgroundColour(wx.Colour(248, 235, 173))

        self.button3 = wx.Button(id=wxID_FRAME1BUTTON3, label='1',
              name='button3', parent=self, pos=wx.Point(128, 208),
              size=wx.Size(56, 72), style=wx.NO_BORDER)
        self.button3.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Tahoma'))
        self.button3.Enable(False)
        self.button3.SetBackgroundColour(wx.Colour(209, 250, 175))

        self.button5 = wx.Button(id=wxID_FRAME1BUTTON5, label='2',
              name='button5', parent=self, pos=wx.Point(56, 208),
              size=wx.Size(56, 72), style=wx.NO_BORDER)
        self.button5.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Tahoma'))
        self.button5.Enable(False)
        self.button5.SetBackgroundColour(wx.Colour(209, 250, 175))

        self.button6 = wx.Button(id=wxID_FRAME1BUTTON6, label='1',
              name='button6', parent=self, pos=wx.Point(56, 120),
              size=wx.Size(56, 72), style= wx.NO_BORDER)
        self.button6.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Tahoma'))
        self.button6.Enable(False)
        self.button6.SetBackgroundColour(wx.Colour(248, 235, 173))

        self.debugOutputText = wx.TextCtrl(id=wxID_FRAME1DEBUGOUTPUTTEXT,
              name='debugOutputText', parent=self, pos=wx.Point(216, 104),
              size=wx.Size(280, 232), style=wx.TE_MULTILINE,
              value='\xb8\xde\xb7\xb7....')

        self.doRenameCheckBox = wx.CheckBox(id=wxID_FRAME1DORENAMECHECKBOX,
              label='\xb0\xe1\xb0\xfa \xc6\xc4\xc0\xcf \xc0\xcc\xb8\xa7 \xb9\xd9\xb2\xd9\xb1\xe2',
              name='doRenameCheckBox', parent=self, pos=wx.Point(232, 88),
              size=wx.Size(144, 16), style=0)
        self.doRenameCheckBox.SetValue(False)
        self.doRenameCheckBox.SetToolTipString('\xba\xaf\xc8\xaf\xb5\xc8 \xb1\xd7\xb8\xb2\xc0\xc7 \xc6\xc4\xc0\xcf\xb8\xed\xc0\xbb 0000000000.jpg, 0000000001.jpg...\xb0\xb0\xc0\xcc \xb9\xf8\xc8\xa3\xb7\xce \xba\xaf\xb0\xe6\xc7\xd5\xb4\xcf\xb4\xd9.')

        self.mainStatusbar = wx.StatusBar(id=wxID_FRAME1MAINSTATUSBAR,
              name='mainStatusbar', parent=self, style=0)
        self.mainStatusbar.SetBackgroundColour(wx.Colour(220, 233, 235))
        self.mainStatusbar.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.mainStatusbar.SetToolTipString('')
        self.mainStatusbar.SetStatusText('')
        self.SetStatusBar(self.mainStatusbar)

        self.remainTimeGuage = wx.Gauge(id=wxID_FRAME1REMAINTIMEGUAGE,
              name='remainTimeGuage', parent=self.mainStatusbar,
              pos=wx.Point(232, 2), range=100, size=wx.Size(702, 18),
              style=wx.SUNKEN_BORDER | wx.GA_HORIZONTAL)
        self.remainTimeGuage.SetToolTipString('')

    def __init__(self, parent):
        self._init_ctrls(parent)

        ########################################################################
        self.enableDebug = False
        ########################################################################



        ########################################################################
        # global variables
        self.isRunning = False
        self.configuration = None
        self.mainThread = None
        ########################################################################
    


        ##############################################################
        ######################################## 새 버전 체크
        if self.checkNewVersion():
            dlg = wx.SingleChoiceDialog(self, '새 버전이 올라왔습니다. 블로그로 이동하시겠습니까?', '새 버전 확인', ["예", "아니오"])
            try:
                if dlg.ShowModal() == wx.ID_OK:
                    selected = dlg.GetStringSelection()
                    if selected == "예":
                        try:
                            import webbrowser
                            webbrowser.open("""http://www.morcavon.com/1178440429""")
                            self.Close()
                        except Exception, msg:
                            pass
                        
            finally:
                dlg.Destroy()
        ##############################################################



        ########################################################################
        # debug mode check
        if self.enableDebug:
            pass
        else:
            self.debugOutputText.Show(False)
        ########################################################################







        ########################################################################
        # initializing
        self.buttonEnabling()
        self.loadConfig()
        self.SetLabel("%s  Version %s                    www.morcavon.com" % (self.GetLabel(), version))
        ########################################################################



        ########################################################################
        # drop files
        self.DragAcceptFiles(True)
        ########################################################################



        ########################################################################
        # frame style 관련.....
        self.SetIcon(wx.IconFromBitmap(icon.getBitmap()))
        ########################################################################




    def OnAboutMenuAboutmenuwhoitemMenu(self, event):
        # about box 띄우기
        dlg = About(self)
        try:
            result = dlg.ShowModal()
        finally:
            dlg.Destroy()

        event.Skip()




    def OnSelectSrcButtonButton(self, event):
        # 원본 폴더 선택
        dlg = wx.DirDialog(self, message="변환할 파일이 있는 폴더를 선택하세요.", defaultPath=self.configuration.sourceDirectory)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                path = dlg.GetPath()
                self.configuration.sourceDirectory = path
                self.selectSrcButton.SetLabel(path)
        finally:
            dlg.Destroy()

        event.Skip()


    def OnSelectDestButtonButton(self, event):
        # 저장 폴더 선택
        
        dlg = wx.DirDialog(self, message="변환된 파일이 저장될 폴더를 선택하세요.", defaultPath=self.configuration.destDirectory)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                path = dlg.GetPath()
                
                self.configuration.destDirectory = path
                self.selectDestButton.SetLabel(path)
                
        finally:
            dlg.Destroy()

        event.Skip()



    def rootDirCheck(self, path):
        # 루트를 타켓으로 지정하는것은 권장하지 않음....
        retValue = True
        
        if os.path.splitdrive(path)[1] == "\\":
            dlg = wx.MessageDialog(self, '루트 디렉토리를 타겟 폴더로 지정하는것은 권장하지 않습니다. 계속하시겠습니까?', '알림', wx.YES_NO | wx.ICON_INFORMATION)
            try:
                result = dlg.ShowModal()
                if result == wx.ID_YES:
                    retValue = True
                else:
                    retValue = False
            finally:
                dlg.Destroy()
        
        
        if self.enableDebug:
            print "rootDirCheck: retvalue =", retValue        
        
        return retValue





    def OnStartButtonButton(self, event):
        # 시작 버튼 클릭

        # 폴더 선택 체크
        if not (os.path.exists(self.selectSrcButton.GetLabel()) and os.path.exists(self.selectDestButton.GetLabel())):
            dlg = wx.MessageDialog(self, '원본 폴더와 저장 폴더를 선택하세요.', '오류', wx.OK | wx.ICON_INFORMATION)
            try:
                result = dlg.ShowModal()
            finally:
                dlg.Destroy()
                return
            
            
        # 현재 설정값 저장
        self.saveConfig()
        
        
        # 루트 디렉토리를 타켓으로 설정했는지 체크
        if not self.rootDirCheck(self.configuration.destDirectory):
            return
        
        
        # 소스와 타켓이 같은 경우 경고 (더 이상 진행 시키지 않음)
        if self.configuration.sourceDirectory == self.configuration.destDirectory:
            dlg = wx.MessageDialog(self, '원본 폴더와 저장 폴더는 달라야 합니다.', '경고', wx.OK | wx.ICON_STOP)
            try:
                result = dlg.ShowModal()
            finally:
                dlg.Destroy()
                return
        
        

    
        # 변환 시작
        self.isRunning = True
        self.mainThread = MainThread(self)
        self.mainThread.start()

        # 버튼 처리
        self.buttonEnabling()




    def OnStopButtonButton(self, event):
        # 중지 버튼 클릭
        if self.enableDebug:
            print "stop button clicked"
        
        self.isRunning = False

        # 버튼 처리
        self.buttonEnabling()

        self.outputText.AppendText("\n\n사용자에 의해 작업이 중단 되었습니다.\n")




    def buttonEnabling(self):
        # 현재 실행 상태에 맞게 버튼 활성화 시킴
##        print dir(self)
##        time.sleep(1)       # 
        
        if self.isRunning:
            enabling = False
        else:
            enabling = True

        self.selectSrcButton.Enable(enabling)
        self.selectDestButton.Enable(enabling)
        self.startButton.Enable(enabling)
        self.stopButton.Enable(not enabling)

        self.jpgRadioButton.Enable(enabling)
        self.zipRadioButton.Enable(enabling)

        self.pictureOrderLeftFirstRadioButton.Enable(enabling)
        self.pictureOrderRightFirstRadioButton.Enable(enabling)

        self.enableCropCheckBox.Enable(enabling)
        self.enableSplitCheckbox.Enable(enabling)
        self.enableZipCompressCheckBox.Enable(enabling)
        self.enableSplitCheckbox.Enable(enabling)
        self.enableLongSideSizeCheckBox.Enable(enabling)

        self.longSideSizeComboBox.Enable(enabling)
        self.splitSizeComboBox.Enable(enabling)






    def saveConfig(self):
        # 현재 설정 상태 저장
        if self.configuration == None:
            return
        
        self.configuration.sourceDirectory = self.selectSrcButton.GetLabel()
        self.configuration.destDirectory = self.selectDestButton.GetLabel()

        self.configuration.fileType = "jpg" if self.jpgRadioButton.GetValue() else "zip"

        self.configuration.pictureOrder = "left" if self.pictureOrderLeftFirstRadioButton.GetValue() else "right"

        self.configuration.doCrop = self.enableCropCheckBox.GetValue()
        self.configuration.doResize = self.enableLongSideSizeCheckBox.GetValue()
        self.configuration.resizeSize = int(self.longSideSizeComboBox.GetValue())

        self.configuration.doZip = self.enableZipCompressCheckBox.GetValue()
        self.configuration.doZipSplit = self.enableSplitCheckbox.GetValue()
        self.configuration.zipSplitSize = int(self.splitSizeComboBox.GetValue())

        self.configuration.doRename = self.doRenameCheckBox.GetValue()


        Config.saveConfig(self.configuration)



    def loadConfig(self):
        # 설정 파일 로드 (없으면 새로 생성)
        self.configuration = Config.getConfig(version)

        self.selectSrcButton.SetLabel(self.configuration.sourceDirectory)
        self.selectDestButton.SetLabel(self.configuration.destDirectory)

        if self.configuration.fileType == "jpg":
            self.jpgRadioButton.SetValue(True)
        else:
            self.zipRadioButton.SetValue(True)

        if self.configuration.pictureOrder == "left":
            self.pictureOrderLeftFirstRadioButton.SetValue(True)
        else:
            self.pictureOrderRightFirstRadioButton.SetValue(True)

        self.enableCropCheckBox.SetValue(self.configuration.doCrop)
        self.enableLongSideSizeCheckBox.SetValue(self.configuration.doResize)
        self.longSideSizeComboBox.SetValue(str(self.configuration.resizeSize))

        self.enableZipCompressCheckBox.SetValue(self.configuration.doZip)
        self.enableSplitCheckbox.SetValue(self.configuration.doZipSplit)
        self.splitSizeComboBox.SetValue(str(self.configuration.zipSplitSize))

        self.doRenameCheckBox.SetValue(self.configuration.doRename)




    def checkNewVersion(self):
        # 업데이트 체크 관련

        if self.enableDebug:
            return False

        try:
            contents = urllib.urlopen("http://www.morcavon.com/1178440429").read()
            rex = """a href=\"/tag/.+?>ver (.+?)</a>"""
            newVersion = re.compile(rex).findall(contents)[0]
        except:
            print "version reading error"
            return False

        # 버전 넘버 체크 (x.x.xx)
        for idx, newNumber in enumerate(newVersion.split(".")):
            if int(version.split(".")[idx]) < int(newNumber):
                # 새 버전 확인!!!
                return True
        return False


    def OnFrame1DropFiles(self, event):
        """ 파일이나 폴더를 드래그&드랍 했을때, sourceDirectory를 변경하고 fileType도 그에 맞게 변경
        """


        if event.GetNumberOfFiles() > 1:
            dlg = wx.MessageDialog(self, '폴더 혹은 zip 파일 하나만 드랍하세요.', '알림', wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)
            try:
                result = dlg.ShowModal()
            finally:
                dlg.Destroy()

        else:
            fileOrDir = event.GetFiles()[0]

            # sourceDirectory 변경
            self.selectSrcButton.SetLabel(os.path.split(fileOrDir)[0] if not os.path.isdir(fileOrDir) else fileOrDir)

            # fileType 변경
            if not os.path.isdir(fileOrDir):        # 드랍된게 폴더인 경우, 타입 변경하지 않음
                if not fileOrDir.lower().endswith(".zip"):
                    dlg = wx.MessageDialog(self, '폴더 혹은 zip 파일 하나만 드랍하세요.', '알림', wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)
                    try:
                        result = dlg.ShowModal()
                    finally:
                        dlg.Destroy()
                else:
                    self.zipRadioButton.SetValue(True)


        event.Skip()





    def OnFrame1Close(self, event):
        # 종료 할 때.....



        # 현재 설정 저장
        self.saveConfig()


        # 임시 파일 삭제
        for root, dlist, flist in os.walk(os.getcwd()):
            for fname in filter(lambda x: x.endswith(".tmp"), flist):
                try:
                    os.remove(os.path.join(root, fname))
                except:
                    pass
    
        event.Skip()




if __name__ == "__main__":
    if os.path.exists("comics4pmp.py"):
        os.system("comics4pmp.py")
    else:
        os.system("comics4pmp.pyw")
