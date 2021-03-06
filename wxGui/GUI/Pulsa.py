#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 9a4613e7dab8 on Sat May  6 08:51:59 2017
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
        self.button_2 = wx.Button(self.panel_1, wx.ID_ANY, _("Ok (Lanjut)"))
        self.button_1 = wx.Button(self.panel_1, wx.ID_ANY, _("Batal"))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: BingkaiPenjualan.__set_properties
        self.SetTitle(_("frame"))
        self.text_ctrl_1.SetFont(wx.Font(50, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Noto Sans"))
        self.text_ctrl_2.SetFont(wx.Font(50, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Noto Sans"))
        self.button_2.SetMinSize((130, 58))
        self.button_2.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Noto Sans"))
        self.button_1.SetMinSize((130, 58))
        self.button_1.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Noto Sans"))
        self.panel_1.SetBackgroundColour(wx.Colour(175, 202, 255))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: BingkaiPenjualan.__do_layout
        self.sizer_1 = wx.BoxSizer(wx.VERTICAL)
        self.sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        self.grid_sizer_2 = wx.GridSizer(1, 2, 0, 10)
        grid_sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        label_3 = wx.StaticText(self.panel_1, wx.ID_ANY, _("Form Pengisian Pulsa"))
        label_3.SetFont(wx.Font(40, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Noto Sans"))
        self.sizer_2.Add(label_3, 0, wx.ALIGN_CENTER | wx.TOP, 40)
        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, _("Nominal"))
        label_1.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Noto Sans"))
        grid_sizer_1.Add(label_1, 0, wx.ALIGN_CENTER | wx.LEFT, 10)
        grid_sizer_1.Add(self.text_ctrl_1, 2, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, 5)
        label_2 = wx.StaticText(self.panel_1, wx.ID_ANY, _("Nomor Pulsa"))
        label_2.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Noto Sans"))
        grid_sizer_1.Add(label_2, 0, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, 5)
        grid_sizer_1.Add(self.text_ctrl_2, 6, wx.ALIGN_CENTER | wx.RIGHT, 10)
        self.sizer_2.Add(grid_sizer_1, 1, wx.ALL | wx.EXPAND, 0)
        self.grid_sizer_2.Add(self.button_2, 0, wx.ALIGN_CENTER, 0)
        self.grid_sizer_2.Add(self.button_1, 0, wx.ALIGN_CENTER, 0)
        sizer_3.Add(self.grid_sizer_2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.RIGHT, 10)
        self.sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
        self.panel_1.SetSizer(self.sizer_2)
        self.sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(self.sizer_1)
        self.sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

# end of class BingkaiPenjualan
