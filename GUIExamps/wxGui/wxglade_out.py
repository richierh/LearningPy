#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade aa26ff80e55e on Fri Mar  3 08:02:48 2017
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
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.panel_3 = wx.Panel(self, wx.ID_ANY)
        self.grid_1 = wx.grid.Grid(self.panel_3, wx.ID_ANY, size=(1, 1))
        self.panel_2 = wx.Panel(self, wx.ID_ANY)
        
        # Menu Bar
        self.frame_menubar = wx.MenuBar()
        self.SetMenuBar(self.frame_menubar)
        # Menu Bar end
        
        # Tool Bar
        self.frame_toolbar = wx.ToolBar(self, -1)
        self.SetToolBar(self.frame_toolbar)
        # Tool Bar end

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle(_("Data Personal"))
        self.SetSize((400, 300))
        self.grid_1.CreateGrid(10, 5)
        self.grid_1.SetRowLabelSize(25)
        self.grid_1.EnableEditing(0)
        self.grid_1.SetGridLineColour(wx.Colour(255, 15, 0))
        self.grid_1.SetLabelBackgroundColour(wx.Colour(113, 255, 26))
        self.grid_1.SetColLabelValue(0, _("No Id"))
        self.grid_1.SetColLabelValue(1, _("Nama"))
        self.grid_1.SetColSize(1, 500)
        self.grid_1.SetColLabelValue(2, _("J/K"))
        self.grid_1.SetColLabelValue(3, _("Tempat lahir"))
        self.grid_1.SetColLabelValue(4, _("Tanggal Lahir"))
        self.grid_1.SetMinSize((1000, 1000))
        self.grid_1.SetBackgroundColour(wx.Colour(201, 255, 132))
        self.panel_3.SetBackgroundColour(wx.Colour(106, 255, 69))
        self.frame_toolbar.Realize()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.FlexGridSizer(1, 3, 0, 0)
        sizer_2 = wx.FlexGridSizer(1, 1, 0, 0)
        grid_sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        sizer_2.Add(self.grid_1, 1, wx.EXPAND, 0)
        self.panel_3.SetSizer(sizer_2)
        grid_sizer_1.Add(self.panel_3, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(self.panel_2, 1, wx.EXPAND, 0)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        self.Centre()
        self.SetSize((400, 300))
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