#!usr/bin/env python
# -*- coding: utf-8 -*-
import wx

class listcontrol(wx.ListCtrl):
    
    def __init__(self,*args,**kwargs):
        super(listcontrol,self).__init__(*args,**kwargs)
        self.InsertColumn(0,"hallo")
        self.InsertColumn(1,"barang")
