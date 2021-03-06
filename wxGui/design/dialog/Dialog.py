#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 9a4613e7dab8 on Fri Apr 14 19:25:45 2017
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        wx.Dialog.__init__(self, *args, **kwds)
        self.window_1 = Text(self, wx.ID_ANY)
        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.button_1 = wx.Button(self, wx.ID_ANY, _("button_1"))
        self.button_2 = wx.Button(self, wx.ID_ANY, _("button_2"))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyDialog.__set_properties
        self.SetTitle(_("dialog"))
        self.SetSize((400, 300))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyDialog.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(self.window_1, 3, wx.EXPAND, 0)
        sizer_2.Add(self.panel_1, 3, wx.EXPAND, 0)
        sizer_2.Add(self.button_1, 1, wx.ALIGN_CENTER, 0)
        sizer_2.Add(self.button_2, 1, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, 7)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

# end of class MyDialog
