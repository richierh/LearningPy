#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.7.2 on Sun Oct  2 11:21:49 2016
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame1(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame1.__init__
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.button_3 = wx.Button(self.panel_1, wx.ID_ANY, _("button_3"))
        self.button_4 = wx.Button(self.panel_1, wx.ID_ANY, _("button_4"))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame1.__set_properties
        self.SetTitle(_("frame_2"))
        self.SetSize((600, 600))
        self.button_3.SetMinSize((150, 150))
        self.button_4.SetMinSize((150, 150))
        self.panel_1.SetMinSize((600, 595))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame1.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(1, 2, 0, 0)
        grid_sizer_1.Add(self.button_3, 0, 0, 0)
        grid_sizer_1.Add(self.button_4, 0, 0, 0)
        sizer_3.Add(grid_sizer_1, 1, 0, 0)
        self.panel_1.SetSizer(sizer_3)
        sizer_2.Add(self.panel_1, 1, 0, 0)
        self.SetSizer(sizer_2)
        self.Layout()
        # end wxGlade

# end of class MyFrame1
if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.PySimpleApp()
    frame_2 = MyFrame1(None, wx.ID_ANY, "")
    app.SetTopWindow(frame_2)
    frame_2.Show()
    app.MainLoop()