#Boa:Dialog:About

import wx

def create(parent):
    return About(parent)

[wxID_ABOUT, wxID_ABOUTSTATICTEXT1, 
] = [wx.NewId() for _init_ctrls in range(2)]

class About(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_ABOUT, name='About', parent=prnt,
              pos=wx.Point(560, 355), size=wx.Size(408, 210),
              style=wx.DEFAULT_DIALOG_STYLE, title='\xb8\xb8\xb5\xe7\xc0\xcc')
        self.SetClientSize(wx.Size(392, 174))
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        #self.SetToolTipString("\xbf\xb5\xbd\xc5\xbe\xc6 \xbb\xe7\xb6\xfb\xc7\xd8~\xa2\xbd")

        self.staticText1 = wx.StaticText(id=wxID_ABOUTSTATICTEXT1,
              label='morcavon', name='staticText1', parent=self,
              pos=wx.Point(155, 16), size=wx.Size(82, 23), style=0)
        self.staticText1.Center(wx.HORIZONTAL)
        self.staticText1.SetCursor(wx.CROSS_CURSOR)
        self.staticText1.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.staticText1.SetForegroundColour(wx.Colour(128, 128, 255))
        self.staticText1.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

    def __init__(self, parent):
        self._init_ctrls(parent)

        self.hyperlink = wx.HyperlinkCtrl(self, 100, "http://www.morcavon.com", "http://www.morcavon.com/1178440429", size=wx.Size(390,30))
        self.hyperlink.Center(wx.BOTH)
        self.hyperlink.SetCursor(wx.CROSS_CURSOR)
        self.hyperlink.SetToolTipString('\xba\xed\xb7\xce\xb1\xd7\xb7\xce GoGo~')
        self.hyperlink.SetForegroundColour(wx.Colour(255, 0, 0))
        self.hyperlink.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Tahoma'))
        self.hyperlink.SetVisitedColour(wx.Colour(0,0,0))
