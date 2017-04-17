#!usr/bin/env python
# -*- coding: utf-8 -*-
#import MyFrame
import MyDialog
import wx
import app
 
class AplikasiRun(app.MyApp):
    
    def __init__(self):
        super(AplikasiRun,self).__init__()
           
    def pilihan_lainnya(self,event):
        print "okayff"
        self.buka = MyDialog.MyDialog(None, wx.ID_ANY, "")
    
    def sukasuka():
        print "ssss"

t = AplikasiRun()
t.MainLoop()