#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 9a4613e7dab8 on Sun Apr 16 17:59:07 2017
#

# This is an automatically generated file.
# Manual changes will be overwritten without warning!

import wx
from MyFrame import MyFrame

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(frame)
        frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()