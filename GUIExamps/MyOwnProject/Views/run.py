#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade aa26ff80e55e on Wed Mar 15 07:48:10 2017
#

# This is an automatically generated file.
# Manual changes will be overwritten without warning!

import wx
import gettext
from RangkaUtama import RangkaUtama

class __main__(wx.App):
    def OnInit(self):
        BukaRangka = RangkaUtama(None, wx.ID_ANY, "")
        self.SetTopWindow(BukaRangka)
        BukaRangka.Show()
        return True

# end of class __main__

if __name__ == "__main__":
    gettext.install("run") # replace with the appropriate catalog name

    run = koleksievent(0)
    run.MainLoop()
    