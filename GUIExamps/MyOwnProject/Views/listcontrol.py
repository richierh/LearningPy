#!usr/bin/env python
# -*- coding: utf-8 -*-
import wx

class listcontrol(wx.ListCtrl):
    
    def __init__(self,*args,**kwargs):
        super(listcontrol,self).__init__(*args,**kwargs)
        self.InsertColumn(0,"KODE BARANG",width=150)
        self.InsertColumn(1,"NAMA BARAMG",width=250)
        self.InsertColumn(2,"JUMLAH",width=75)
        self.InsertColumn(3,"HARGA",width=150)
        self.InsertColumn(4,"TOTAL",width=200)
      
        