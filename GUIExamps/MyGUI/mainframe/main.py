#! /usr/bin/python
import wx
import gettext
from mainframe.fungsievent import *
import mainframe
print ("hhh")

class MyApp(wx.App):
    def OnInit(self):
        self.frame = FFormEvent(None)
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True


if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = MyApp(0)
    app.MainLoop()
