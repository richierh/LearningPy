#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 9a4613e7dab8 on Wed Apr 26 06:03:49 2017 from "/home/richie/mygit/LearningPy/wxGui/FormPulsa.wxg"
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class BingkaiPenjualan(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: BingkaiPenjualan.__init__
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.text_ctrl_1 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.text_ctrl_2 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: BingkaiPenjualan.__set_properties
        self.SetTitle(_("frame"))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: BingkaiPenjualan.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        self.sizer_2 = wx.FlexGridSizer(2, 1, 0, 0)
        grid_sizer_1 = wx.FlexGridSizer(1, 4, 0, 10)
        label_3 = wx.StaticText(self.panel_1, wx.ID_ANY, _("label_3"))
        label_3.SetFont(wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Noto Sans"))
        self.sizer_2.Add(label_3, 0, wx.ALIGN_CENTER, 0)
        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, _("label_1"))
        grid_sizer_1.Add(label_1, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_1.Add(self.text_ctrl_1, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        label_2 = wx.StaticText(self.panel_1, wx.ID_ANY, _("label_2"))
        grid_sizer_1.Add(label_2, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_1.Add(self.text_ctrl_2, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.AddGrowableRow(0)
        grid_sizer_1.AddGrowableCol(1)
        grid_sizer_1.AddGrowableCol(3)
        self.sizer_2.Add(grid_sizer_1, 1, wx.ALL | wx.EXPAND, 10)
        self.panel_1.SetSizer(self.sizer_2)
        self.sizer_2.AddGrowableRow(0)
        self.sizer_2.AddGrowableRow(1)
        self.sizer_2.AddGrowableCol(0)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

# end of class BingkaiPenjualan
