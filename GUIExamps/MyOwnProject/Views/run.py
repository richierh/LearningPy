#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
<<<<<<< HEAD
# generated by wxGlade aa26ff80e55e on Wed Mar 15 07:48:10 2017
=======
# generated by wxGlade 9a4613e7dab8 on Thu Apr 13 12:51:52 2017
>>>>>>> 7699f563a787b17d670dbeec96460ca3b05904c6
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

<<<<<<< HEAD
    run = koleksievent(0)
    run.MainLoop()
    
=======
    run = __main__(0)
    run.MainLoop()
>>>>>>> 7699f563a787b17d670dbeec96460ca3b05904c6
