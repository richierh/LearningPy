# -*- coding: UTF-8 -*-
#
# generated by wxGlade 9a4613e7dab8 on Sat Apr 15 11:29:39 2017
#

import wx
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = wx.CLOSE_BOX
        wx.Dialog.__init__(self, *args, **kwds)
        self.button_7 = wx.Button(self, wx.ID_ANY, "button_7")
        self.button_8 = wx.Button(self, wx.ID_ANY, "button_7")
        self.button_9 = wx.Button(self, wx.ID_ANY, "button_7")
        self.button_10 = wx.Button(self, wx.ID_ANY, "button_7")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyDialog.__set_properties
        self.SetTitle("dialog")
        self.button_7.SetMinSize((125, 64))
        self.button_8.SetMinSize((125, 64))
        self.button_9.SetMinSize((125, 64))
        self.button_10.SetMinSize((125, 64))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyDialog.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_3 = wx.FlexGridSizer(2, 2, 0, 0)
        label_4 = wx.StaticText(self, wx.ID_ANY, "Pilihan anda ?")
        sizer_2.Add(label_4, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_3.Add(self.button_7, 0, wx.ALL, 5)
        grid_sizer_3.Add(self.button_8, 0, wx.ALL, 5)
        grid_sizer_3.Add(self.button_9, 0, wx.ALL, 5)
        grid_sizer_3.Add(self.button_10, 0, wx.ALL, 5)
        sizer_2.Add(grid_sizer_3, 2, wx.EXPAND, 0)
        self.SetSizer(sizer_2)
        sizer_2.Fit(self)
        self.Layout()
        # end wxGlade

# end of class MyDialog
