# -*- coding: UTF-8 -*-
#
# generated by wxGlade 9a4613e7dab8 on Sun Apr 16 17:54:01 2017
#

import wx
# begin wxGlade: dependencies
import wx.grid
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        
        # Menu Bar
        self.frame_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.ID_ANY, "item", "")
        wxglade_tmp_menu.Append(wx.ID_ANY, "item", "")
        self.frame_menubar.Append(wxglade_tmp_menu, "item")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.ID_ANY, "item", "")
        wxglade_tmp_menu.Append(wx.ID_ANY, "item", "")
        self.frame_menubar.Append(wxglade_tmp_menu, "item")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.ID_ANY, "item", "")
        self.frame_menubar.Append(wxglade_tmp_menu, "item")
        self.SetMenuBar(self.frame_menubar)
        # Menu Bar end
        self.frame_statusbar = self.CreateStatusBar(1)
        
        # Tool Bar
        self.frame_toolbar = wx.ToolBar(self, -1, style=wx.TB_HORIZONTAL | wx.TB_NOICONS | wx.TB_TEXT)
        self.SetToolBar(self.frame_toolbar)
        self.frame_toolbar.AddLabelTool(wx.ID_ANY, "item", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, "", "")
        self.frame_toolbar.AddLabelTool(wx.ID_ANY, "item", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, "", "")
        self.frame_toolbar.AddLabelTool(wx.ID_ANY, "item", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, "", "")
        self.frame_toolbar.AddLabelTool(wx.ID_ANY, "item", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, "", "")
        self.frame_toolbar.AddLabelTool(wx.ID_ANY, "item", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, "", "")
        # Tool Bar end
        self.notebook_1 = wx.Notebook(self, wx.ID_ANY, style=wx.NB_LEFT)
        self.Menu_Utama = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.Penjualan = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.panel_3 = wx.Panel(self.Penjualan, wx.ID_ANY)
        self.text_ctrl_1 = wx.TextCtrl(self.Penjualan, wx.ID_ANY, "")
        self.text_ctrl_2 = wx.TextCtrl(self.Penjualan, wx.ID_ANY, "1", style=wx.TE_CENTRE)
        self.button_2 = wx.Button(self.Penjualan, wx.ID_ADD, "")
        self.list_ctrl_1 = wx.ListCtrl(self.Penjualan, wx.ID_ANY, style=wx.BORDER_DEFAULT | wx.BORDER_SUNKEN | wx.LC_REPORT | wx.NO_FULL_REPAINT_ON_RESIZE)
        self.button_3 = wx.Button(self.Penjualan, wx.ID_ANY, "Cetak & Simpan")
        self.button_1 = wx.Button(self.Penjualan, wx.ID_ANY, "Cetak Saja")
        self.button_4 = wx.Button(self.Penjualan, wx.ID_ANY, "Hapus")
        self.button_5 = wx.Button(self.Penjualan, wx.ID_ANY, "Lihat")
        self.button_6 = wx.Button(self.Penjualan, wx.ID_ANY, "Pilihan Lainnya", style=wx.BU_EXACTFIT)
        self.Data_Barang = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.grid_1 = wx.grid.Grid(self.Data_Barang, wx.ID_ANY, size=(1, 1))
        self.Data_Pekerja = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.Pengaturan = wx.Panel(self.notebook_1, wx.ID_ANY)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.Input, self.button_2)
        self.Bind(wx.EVT_BUTTON, self.pilihan_lainnya, self.button_6)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("frame")
        self.SetSize((1360, 737))
        self.frame_statusbar.SetStatusWidths([-1])

        # statusbar fields
        frame_statusbar_fields = ["Status"]
        for i in range(len(frame_statusbar_fields)):
            self.frame_statusbar.SetStatusText(frame_statusbar_fields[i], i)
        self.frame_toolbar.Realize()
        self.panel_3.SetBackgroundColour(wx.Colour(255, 255, 0))
        self.text_ctrl_1.SetMinSize((200, 34))
        self.button_3.SetMinSize((150, 34))
        self.button_1.SetMinSize((150, 34))
        self.button_4.SetMinSize((150, 34))
        self.button_5.SetMinSize((150, 34))
        self.button_6.SetMinSize((150, 34))
        self.grid_1.CreateGrid(10, 5)
        self.grid_1.EnableEditing(0)
        self.grid_1.SetColLabelValue(0, "KODE BARANG")
        self.grid_1.SetColSize(0, 150)
        self.grid_1.SetColLabelValue(1, "NAMA BARANG")
        self.grid_1.SetColSize(1, 300)
        self.grid_1.SetColLabelValue(2, "SATUAN")
        self.grid_1.SetColSize(2, 75)
        self.grid_1.SetColLabelValue(3, " HARGA\n SATUAN")
        self.grid_1.SetColSize(3, 100)
        self.grid_1.SetColLabelValue(4, "KETERANGAN")
        self.grid_1.SetColSize(4, 300)
        self.grid_1.SetFocus()
        self.Data_Barang.SetBackgroundColour(wx.Colour(159, 159, 95))
        self.Data_Pekerja.SetBackgroundColour(wx.Colour(159, 159, 95))
        self.Pengaturan.SetBackgroundColour(wx.Colour(159, 159, 95))
        self.notebook_1.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_8 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_2 = wx.GridSizer(5, 1, 0, 0)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.FlexGridSizer(1, 7, 0, 0)
        sizer_7 = wx.BoxSizer(wx.VERTICAL)
        label_2 = wx.StaticText(self, wx.ID_ANY, "APLIKASI PENJUALAN KASIR CANGGIH")
        label_2.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        sizer_3.Add(label_2, 0, wx.ALIGN_CENTER, 0)
        sizer_6.Add((0, 0), 0, 0, 0)
        label_5 = wx.StaticText(self.panel_3, wx.ID_ANY, "0", style=wx.ALIGN_CENTER | wx.ALIGN_RIGHT)
        label_5.SetFont(wx.Font(50, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        sizer_7.Add(label_5, 1, wx.ALIGN_RIGHT, 0)
        self.panel_3.SetSizer(sizer_7)
        sizer_6.Add(self.panel_3, 1, wx.EXPAND, 0)
        label_1 = wx.StaticText(self.Penjualan, wx.ID_ANY, "Kode Barang")
        grid_sizer_1.Add(label_1, 0, wx.ALIGN_CENTER | wx.LEFT, 8)
        grid_sizer_1.Add(self.text_ctrl_1, 0, wx.LEFT | wx.RIGHT, 8)
        label_3 = wx.StaticText(self.Penjualan, wx.ID_ANY, "Jumlah")
        grid_sizer_1.Add(label_3, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_1.Add(self.text_ctrl_2, 0, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, 8)
        grid_sizer_1.Add(self.button_2, 0, wx.RIGHT, 8)
        sizer_6.Add(grid_sizer_1, 0, wx.EXPAND, 0)
        sizer_4.Add(sizer_6, 1, wx.EXPAND, 0)
        sizer_5.Add(self.list_ctrl_1, 5, wx.EXPAND, 0)
        grid_sizer_2.Add(self.button_3, 0, 0, 0)
        grid_sizer_2.Add(self.button_1, 0, 0, 0)
        grid_sizer_2.Add(self.button_4, 0, 0, 0)
        grid_sizer_2.Add(self.button_5, 0, 0, 0)
        grid_sizer_2.Add(self.button_6, 0, 0, 0)
        sizer_5.Add(grid_sizer_2, 0, wx.LEFT | wx.RIGHT, 10)
        sizer_4.Add(sizer_5, 4, wx.EXPAND, 0)
        self.Penjualan.SetSizer(sizer_4)
        sizer_8.Add((0, 0), 0, 0, 0)
        sizer_8.Add(self.grid_1, 3, wx.EXPAND, 0)
        self.Data_Barang.SetSizer(sizer_8)
        self.notebook_1.AddPage(self.Menu_Utama, "Menu Utama")
        self.notebook_1.AddPage(self.Penjualan, "Penjualan")
        self.notebook_1.AddPage(self.Data_Barang, "Data Barang")
        self.notebook_1.AddPage(self.Data_Pekerja, "Data Pekerja")
        self.notebook_1.AddPage(self.Pengaturan, "Pengaturan")
        sizer_3.Add(self.notebook_1, 5, wx.ALIGN_CENTER | wx.EXPAND, 0)
        self.SetSizer(sizer_3)
        self.Layout()
        self.Centre()
        self.SetSize((1360, 737))
        # end wxGlade

    def Input(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'Input' not implemented!")
        event.Skip()

    def pilihan_lainnya(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'pilihan_lainnya' not implemented!")
        event.Skip()

# end of class MyFrame
