# -*- coding: UTF-8 -*-
#
<<<<<<< HEAD
# generated by wxGlade aa26ff80e55e on Wed Mar 15 07:55:42 2017
=======
# generated by wxGlade 9a4613e7dab8 on Thu Apr 13 12:51:52 2017
>>>>>>> 7699f563a787b17d670dbeec96460ca3b05904c6
#

import wx
# begin wxGlade: dependencies
import wx.grid
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class RangkaUtama(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: RangkaUtama.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL
        wx.Frame.__init__(self, *args, **kwds)
<<<<<<< HEAD
        self.panel_2 = wx.Panel(self, wx.ID_ANY)
        self.panel_3 = wx.Panel(self.panel_2, wx.ID_ANY)
        self.TabelNotebook1 = wx.Notebook(self.panel_2, wx.ID_ANY, style=wx.NB_LEFT)
        self.Barang = wx.Panel(self.TabelNotebook1, wx.ID_ANY)
        self.text_ctrl_1 = wx.TextCtrl(self.Barang, wx.ID_ANY, "")
        self.button_1 = wx.Button(self.Barang, wx.ID_ANY, _("Cari"), style=wx.BU_AUTODRAW)
        self.grid_1 = wx.grid.Grid(self.Barang, wx.ID_ANY, size=(1, 1))
        self.Penjualan = wx.Panel(self.TabelNotebook1, wx.ID_ANY)
        self.list_ctrl_1 = wx.ListCtrl(self.Penjualan, wx.ID_ANY, style=wx.BORDER_DEFAULT | wx.BORDER_SUNKEN | wx.LC_REPORT | wx.NO_FULL_REPAINT_ON_RESIZE)
        self.Bantuan = wx.Panel(self.TabelNotebook1, wx.ID_ANY)
=======
>>>>>>> 7699f563a787b17d670dbeec96460ca3b05904c6
        
        # Menu Bar
        self.BukaRangka_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
<<<<<<< HEAD
        item = wxglade_tmp_menu.Append(2, _("Keluar"), "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, self.Keluar, id=item.GetId())
        self.BukaRangka_menubar.Append(wxglade_tmp_menu, _("Berkas"))
        wxglade_tmp_menu = wx.Menu()
        item = wxglade_tmp_menu.Append(4, _("BukaRangka1"), "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, self.bukarangka1, id=item.GetId())
        self.BukaRangka_menubar.Append(wxglade_tmp_menu, _("Pengaturan"))
        self.SetMenuBar(self.BukaRangka_menubar)
        # Menu Bar end
=======
        wxglade_tmp_item = wxglade_tmp_menu.Append(2, _("Keluar"), "")
        self.Bind(wx.EVT_MENU, self.Keluar, id=wxglade_tmp_item.GetId())
        self.BukaRangka_menubar.Append(wxglade_tmp_menu, _("Berkas"))
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_item = wxglade_tmp_menu.Append(4, _("BukaRangka1"), "")
        self.Bind(wx.EVT_MENU, self.bukarangka1, id=wxglade_tmp_item.GetId())
        self.BukaRangka_menubar.Append(wxglade_tmp_menu, _("Pengaturan"))
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_item = wxglade_tmp_menu.Append(wx.ID_ANY, _("Tentang"), "")
        self.Bind(wx.EVT_MENU, self.Tentang, id=wxglade_tmp_item.GetId())
        self.BukaRangka_menubar.Append(wxglade_tmp_menu, _("Info"))
        self.SetMenuBar(self.BukaRangka_menubar)
        # Menu Bar end
        self.panel_2 = wx.Panel(self, wx.ID_ANY)
        self.panel_3 = wx.Panel(self.panel_2, wx.ID_ANY)
        self.TabelNotebook1 = wx.Notebook(self.panel_2, wx.ID_ANY, style=wx.NB_LEFT)
        self.Barang = wx.Panel(self.TabelNotebook1, wx.ID_ANY)
        self.text_ctrl_1 = wx.TextCtrl(self.Barang, wx.ID_ANY, "")
        self.button_1 = wx.Button(self.Barang, wx.ID_ANY, _("Cari"), style=wx.BU_AUTODRAW)
        self.grid_1 = wx.grid.Grid(self.Barang, wx.ID_ANY, size=(1, 1))
        self.Penjualan = wx.Panel(self.TabelNotebook1, wx.ID_ANY)
        self.list_ctrl_1 = listcontrol(self.Penjualan, wx.ID_ANY, style=wx.BORDER_DEFAULT | wx.BORDER_SUNKEN | wx.LC_REPORT | wx.NO_FULL_REPAINT_ON_RESIZE)
        self.text_ctrl_2 = wx.TextCtrl(self.Penjualan, wx.ID_ANY, "")
        self.Bantuan = wx.Panel(self.TabelNotebook1, wx.ID_ANY)
>>>>>>> 7699f563a787b17d670dbeec96460ca3b05904c6

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.Yes, self.button_1)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: RangkaUtama.__set_properties
        self.SetTitle(_("Pos Penjualan"))
        self.SetSize((800, 601))
        self.panel_3.SetBackgroundColour(wx.Colour(43, 192, 139))
        self.panel_3.SetForegroundColour(wx.Colour(0, 0, 0))
        self.button_1.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Noto Sans"))
        self.grid_1.CreateGrid(30, 3)
        self.grid_1.SetRowLabelSize(20)
        self.grid_1.EnableEditing(0)
        self.grid_1.SetLabelBackgroundColour(wx.Colour(43, 192, 139))
        self.grid_1.SetColLabelValue(0, _("Kode Barang"))
        self.grid_1.SetColSize(0, 150)
        self.grid_1.SetColLabelValue(1, _("Nama Barang"))
        self.grid_1.SetColSize(1, 300)
        self.grid_1.SetColLabelValue(2, _("Satuan"))
        self.grid_1.SetColSize(2, 100)
        self.grid_1.SetBackgroundColour(wx.Colour(43, 192, 139))
        self.grid_1.SetForegroundColour(wx.Colour(255, 255, 255))
        self.Barang.SetBackgroundColour(wx.Colour(43, 192, 139))
        self.Barang.SetForegroundColour(wx.Colour(0, 0, 0))
        self.Penjualan.SetBackgroundColour(wx.Colour(43, 192, 139))
        self.Penjualan.SetForegroundColour(wx.Colour(255, 255, 255))
        self.Bantuan.SetBackgroundColour(wx.Colour(43, 192, 139))
        self.Bantuan.SetForegroundColour(wx.Colour(0, 0, 0))
        self.TabelNotebook1.SetBackgroundColour(wx.Colour(43, 192, 139))
        self.TabelNotebook1.SetFont(wx.Font(10, wx.DEFAULT, wx.ITALIC, wx.BOLD, 1, ""))
        self.panel_2.SetBackgroundColour(wx.Colour(43, 192, 139))
        self.panel_2.SetForegroundColour(wx.Colour(0, 0, 0))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: RangkaUtama.__do_layout
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_2 = wx.FlexGridSizer(2, 1, 0, 0)
        sizer_4 = wx.FlexGridSizer(1, 1, 0, 0)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
<<<<<<< HEAD
        grid_sizer_1 = wx.FlexGridSizer(3, 1, 0, 0)
=======
        grid_sizer_1 = wx.FlexGridSizer(2, 1, 0, 0)
>>>>>>> 7699f563a787b17d670dbeec96460ca3b05904c6
        grid_sizer_5 = wx.FlexGridSizer(3, 1, 0, 0)
        bagi_ruang_1 = wx.FlexGridSizer(3, 1, 0, 0)
        grid_sizer_4 = wx.FlexGridSizer(1, 3, 0, 10)
        grid_sizer_3 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_3.Add(self.panel_3, 1, wx.EXPAND, 0)
<<<<<<< HEAD
        bitmap_1 = wx.StaticBitmap(self.panel_2, wx.ID_ANY, wx.Bitmap("/home/richie/Pictures/pmcicon.png", wx.BITMAP_TYPE_ANY))
=======
        bitmap_1 = wx.StaticBitmap(self.panel_2, wx.ID_ANY, wx.EmptyBitmap(100, 100))
>>>>>>> 7699f563a787b17d670dbeec96460ca3b05904c6
        bitmap_1.SetMinSize((100, 100))
        grid_sizer_3.Add(bitmap_1, 0, 0, 0)
        grid_sizer_3.AddGrowableCol(0)
        grid_sizer_2.Add(grid_sizer_3, 1, wx.EXPAND, 0)
        label_1 = wx.StaticText(self.Barang, wx.ID_ANY, _("Daftar Barang"), style=wx.ALIGN_CENTER)
        label_1.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Noto Sans"))
        bagi_ruang_1.Add(label_1, 0, wx.ALIGN_CENTER, 0)
        label_2 = wx.StaticText(self.Barang, wx.ID_ANY, _("Kode Barang"))
        label_2.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Noto Sans"))
        grid_sizer_4.Add(label_2, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 11)
        grid_sizer_4.Add(self.text_ctrl_1, 0, wx.EXPAND, 0)
        grid_sizer_4.Add(self.button_1, 1, wx.LEFT, 9)
        grid_sizer_4.AddGrowableCol(1)
        grid_sizer_4.AddGrowableCol(2)
        bagi_ruang_1.Add(grid_sizer_4, 1, wx.ALL | wx.EXPAND, 1)
        bagi_ruang_1.Add(self.grid_1, 0, wx.EXPAND, 0)
        self.Barang.SetSizer(bagi_ruang_1)
        bagi_ruang_1.AddGrowableRow(2)
        bagi_ruang_1.AddGrowableCol(0)
<<<<<<< HEAD
        label_3 = wx.StaticText(self.Penjualan, wx.ID_ANY, _("label_3"), style=wx.ALIGN_CENTER)
        grid_sizer_1.Add(label_3, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_5.Add((0, 0), 0, 0, 0)
        grid_sizer_5.Add(self.list_ctrl_1, 1, wx.EXPAND, 0)
        grid_sizer_5.Add((0, 0), 0, 0, 0)
        grid_sizer_5.AddGrowableRow(1)
        grid_sizer_5.AddGrowableCol(0)
        grid_sizer_1.Add(grid_sizer_5, 1, wx.EXPAND, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        self.Penjualan.SetSizer(grid_sizer_1)
        grid_sizer_1.AddGrowableRow(1)
=======
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_5.Add((0, 0), 0, 0, 0)
        grid_sizer_5.Add(self.list_ctrl_1, 5, wx.EXPAND, 0)
        grid_sizer_5.Add(self.text_ctrl_2, 0, wx.EXPAND, 0)
        grid_sizer_5.AddGrowableRow(1)
        grid_sizer_5.AddGrowableCol(0)
        grid_sizer_1.Add(grid_sizer_5, 1, wx.EXPAND, 0)
        self.Penjualan.SetSizer(grid_sizer_1)
        grid_sizer_1.AddGrowableRow(1)
        grid_sizer_1.AddGrowableCol(0)
>>>>>>> 7699f563a787b17d670dbeec96460ca3b05904c6
        label_4 = wx.StaticText(self.Bantuan, wx.ID_ANY, _("label_4"))
        sizer_6.Add(label_4, 0, 0, 0)
        self.Bantuan.SetSizer(sizer_6)
        self.TabelNotebook1.AddPage(self.Barang, _("Barang"))
        self.TabelNotebook1.AddPage(self.Penjualan, _("Penjualan"))
        self.TabelNotebook1.AddPage(self.Bantuan, _("Bantuan"))
        sizer_4.Add(self.TabelNotebook1, 1, wx.ALL | wx.EXPAND, 2)
        sizer_4.AddGrowableRow(0)
        sizer_4.AddGrowableCol(0)
        grid_sizer_2.Add(sizer_4, 1, wx.EXPAND, 0)
        self.panel_2.SetSizer(grid_sizer_2)
        grid_sizer_2.AddGrowableRow(1)
        grid_sizer_2.AddGrowableCol(0)
        sizer_3.Add(self.panel_2, 1, wx.EXPAND | wx.FIXED_MINSIZE, 0)
        self.SetSizer(sizer_3)
        self.Layout()
        self.Centre()
        self.SetSize((800, 601))
        # end wxGlade

<<<<<<< HEAD
    def Yes(self, event):  # wxGlade: RangkaUtama.<event_handler>
        print("Event handler 'Yes' not implemented!")
        event.Skip()

=======
>>>>>>> 7699f563a787b17d670dbeec96460ca3b05904c6
    def Keluar(self, event):  # wxGlade: RangkaUtama.<event_handler>
        print("Event handler 'Keluar' not implemented!")
        event.Skip()

    def bukarangka1(self, event):  # wxGlade: RangkaUtama.<event_handler>
        print("Event handler 'bukarangka1' not implemented!")
        event.Skip()

<<<<<<< HEAD
# end of class RangkaUtama
=======
    def Yes(self, event):  # wxGlade: RangkaUtama.<event_handler>
        print("Event handler 'Yes' not implemented!")
        event.Skip()

    def Tentang(self, event):  # wxGlade: RangkaUtama.<event_handler>
        print("Event handler 'Tentang' not implemented!")
        from MyDialog import MyDialog
        MyDialog()
        event.Skip()
# end of class RangkaUtama
class listcontrol(wx.ListCtrl):
    
    def __init__(self,*args,**kwargs):
        super(listcontrol,self).__init__(*args,**kwargs)
        self.InsertColumn(0,"KODE BARANG",width=150)
        self.InsertColumn(1,"NAMA BARAMG",width=250)
        self.InsertColumn(2,"JUMLAH",width=75)
        self.InsertColumn(3,"HARGA",width=150)
        self.InsertColumn(4,"TOTAL",width=200)
      
        
>>>>>>> 7699f563a787b17d670dbeec96460ca3b05904c6
