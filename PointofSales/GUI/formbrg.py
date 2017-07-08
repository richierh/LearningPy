#!/usr/bin/env python
import wx


'''Ini adalah Desain Form Barang untuk POS'''

class form(wx.Frame):
    'kelas Form'
    def __init__(self,*args,**kwargs):
        super(form,self).__init__(*args,**kwargs)
        self.SetPosition()
        self.


root = wx.App()
formbrg=form(None,title="Form Barang")
formbrg.Show()
root.MainLoop()
