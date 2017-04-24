#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 9a4613e7dab8 on Mon Apr 24 12:08:38 2017
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.text_ctrl_1 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.label_8 = wx.StaticText(self.panel_1, wx.ID_ANY, _("Nama Barang"))
        self.text_ctrl_2 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.label_9 = wx.StaticText(self.panel_1, wx.ID_ANY, _("Nama 2"))
        self.text_ctrl_3 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.choice_1 = wx.Choice(self.panel_1, wx.ID_ANY, choices=[_("Dus"), _("Buah")])
        self.button_1 = wx.Button(self.panel_1, wx.ID_ANY, _("Tambah"))
        self.label_11 = wx.StaticText(self.panel_1, wx.ID_ANY, _("Harga Jual"))
        self.text_ctrl_4 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.label_12 = wx.StaticText(self.panel_1, wx.ID_ANY, _("Harga Beli"))
        self.text_ctrl_6 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.button_4 = wx.Button(self.panel_1, wx.ID_ANY, _("Ok"))
        self.button_5 = wx.Button(self.panel_1, wx.ID_ANY, _("Cancel"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.form_tambah, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.form_ok, self.button_4)
        self.Bind(wx.EVT_BUTTON, self.form_cancel, self.button_5)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle(_("Form Data Barang"))
        self.text_ctrl_1.SetMinSize((200, 40))
        self.text_ctrl_2.SetMinSize((300, 40))
        self.text_ctrl_3.SetMinSize((300, 40))
        self.choice_1.SetMinSize((84, 40))
        self.choice_1.SetSelection(0)
        self.button_1.SetMinSize((85, 30))
        self.text_ctrl_4.SetMinSize((100, 40))
        self.text_ctrl_6.SetMinSize((100, 40))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        self.sizer_3 = wx.BoxSizer(wx.VERTICAL)
        self.sizer_5 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_3 = wx.FlexGridSizer(1, 2, 0, 10)
        self.grid_sizer_2 = wx.FlexGridSizer(6, 2, 15, 30)
        grid_sizer_1 = wx.FlexGridSizer(1, 2, 0, 15)
        label_17 = wx.StaticText(self.panel_1, wx.ID_ANY, _("Form Data Barang"), style=wx.ALIGN_CENTER)
        label_17.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.sizer_5.Add(label_17, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, _("Kode ID"))
        self.grid_sizer_2.Add(label_1, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        self.grid_sizer_2.Add(self.text_ctrl_1, 0, 0, 0)
        self.grid_sizer_2.Add(self.label_8, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        self.grid_sizer_2.Add(self.text_ctrl_2, 0, 0, 0)
        self.grid_sizer_2.Add(self.label_9, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        self.grid_sizer_2.Add(self.text_ctrl_3, 0, 0, 0)
        label_2 = wx.StaticText(self.panel_1, wx.ID_ANY, _("Satuan"))
        self.grid_sizer_2.Add(label_2, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.choice_1, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_1.Add(self.button_1, 0, wx.ALIGN_CENTER | wx.ALL, 0)
        self.grid_sizer_2.Add(grid_sizer_1, 0, wx.EXPAND, 0)
        self.grid_sizer_2.Add(self.label_11, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        self.grid_sizer_2.Add(self.text_ctrl_4, 0, 0, 0)
        self.grid_sizer_2.Add(self.label_12, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        self.grid_sizer_2.Add(self.text_ctrl_6, 0, 0, 0)
        self.sizer_5.Add(self.grid_sizer_2, 0, wx.ALL | wx.EXPAND, 15)
        grid_sizer_3.Add(self.button_4, 0, 0, 0)
        grid_sizer_3.Add(self.button_5, 0, 0, 0)
        grid_sizer_3.AddGrowableRow(0)
        grid_sizer_3.AddGrowableCol(0)
        grid_sizer_3.AddGrowableCol(1)
        self.sizer_5.Add(grid_sizer_3, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL, 15)
        self.panel_1.SetSizer(self.sizer_5)
        self.sizer_3.Add(self.panel_1, 0, wx.EXPAND, 0)
        self.SetSizer(self.sizer_3)
        self.sizer_3.Fit(self)
        self.Layout()
        # end wxGlade

    def form_tambah(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'form_tambah' not implemented!")
        event.Skip()

    def form_ok(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'form_ok' not implemented!")
        event.Skip()

    def form_cancel(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'form_cancel' not implemented!")
        event.Skip()

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