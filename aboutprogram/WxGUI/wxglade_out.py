#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade f1f66815ed4c on Thu Nov 24 07:24:51 2016
#

import wx
import wx.grid

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.button_1 = wx.Button(self.panel_1, wx.ID_ANY, _("button_1"))
        self.button_2 = wx.Button(self.panel_1, wx.ID_ANY, _("button_2"))
        self.button_3 = wx.Button(self.panel_1, wx.ID_ANY, _("button_3"))
        self.button_4 = wx.Button(self.panel_1, wx.ID_ANY, _("button_4"))
        self.button_5 = wx.Button(self.panel_1, wx.ID_ANY, _("button_5"))
        self.button_6 = wx.Button(self.panel_1, wx.ID_ANY, _("button_6"))
        self.button_7 = wx.Button(self.panel_1, wx.ID_ANY, _("button_7"))
        self.button_8 = wx.Button(self.panel_1, wx.ID_ANY, _("button_8"))
        self.button_9 = wx.Button(self.panel_1, wx.ID_ANY, _("button_9"))
        self.grid_1 = wx.grid.Grid(self.panel_1, wx.ID_ANY, size=(1, 1))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle(_("frame"))
        self.grid_1.CreateGrid(10, 3)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_1 = wx.GridSizer(3, 3, 0, 0)
        grid_sizer_1.Add(self.button_1, 0, 0, 0)
        grid_sizer_1.Add(self.button_2, 0, 0, 0)
        grid_sizer_1.Add(self.button_3, 0, 0, 0)
        grid_sizer_1.Add(self.button_4, 0, 0, 0)
        grid_sizer_1.Add(self.button_5, 0, 0, 0)
        grid_sizer_1.Add(self.button_6, 0, 0, 0)
        grid_sizer_1.Add(self.button_7, 0, 0, 0)
        grid_sizer_1.Add(self.button_8, 0, 0, 0)
        grid_sizer_1.Add(self.button_9, 0, 0, 0)
        sizer_2.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        sizer_2.Add(self.grid_1, 1, wx.EXPAND, 0)
        self.panel_1.SetSizer(sizer_2)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        sizer_1.SetSizeHints(self)
        self.Layout()
        # end wxGlade

# end of class MyFrame
class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(frame)
        frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = MyApp(0)
    app.MainLoop()