#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade aa26ff80e55e on Tue Mar 14 08:01:28 2017
#

# This is an automatically generated file.
# Manual changes will be overwritten without warning!

import wx
import gettext
from Layar3 import Layar3

class Main(wx.App):
    def OnInit(self):
        frame_2 = Layar3(None, wx.ID_ANY, "")
        self.SetTopWindow(frame_2)
        frame_2.Show()
        return True

# end of class Main

if __name__ == "__main__":
    gettext.install("myapp") # replace with the appropriate catalog name

    myapp = Main(0)
    myapp.MainLoop()