#!usr/bin/env python
# -*- coding: utf-8 -*-

import wx


class Maunggak():
    
    pass

class FrameCtrl(wx.Frame):
    
    def __init__(self,*args,**kwargs):
        super(FrameCtrl,self).__init__(*args,**kwargs)
        self.SetTitle("okay")
        self.Centre()
        self.SetToolTipString("test")
        self.SetClass()
        self.SetCursor(wx.StockCursor(wx.CURSOR_MAGNIFIER))
        self.Maximize(False)
        
    def SetClass(self):
        
        pass
    

if __name__=="__main__":
    
    root=wx.App()
    frame = FrameCtrl(None,wx.ID_ANY,"")
    frame.Show()
    root.MainLoop()