#!/usr/bin/env python

# spreadsheet.py

import wx
from wx.lib import sheet


class MySheet(sheet.CSheet):
    def __init__(self, parent):
        sheet.CSheet.__init__(self, parent)
        self.row = self.col = 0
        self.SetNumberRows(55)
        self.SetNumberCols(25)

        for i in range(55):
            self.SetRowSize(i, 20)

    def OnGridSelectCell(self, event):
        self.row, self.col = event.GetRow(), event.GetCol()
        control = self.GetParent().GetParent().position
        value =  self.GetColLabelValue(self.col) + self.GetRowLabelValue(self.row)
        control.SetValue(value)
        event.Skip()

class MyFrame(wx.Frame):
    
    def __init__(self,*args,**kwargs):
        super(MyFrame,self).__init__(*args,**kwargs)
        self.SetTitle("Hallo")
        sizer = wx.BoxSizer(wx.VERTICAL)
        c = sizer.add(MySheet,1,wx.EXPAND,0)
        SetSizer(c)
        
        

if __name__=="__main__":
    app =  wx.App(True)
    frame = MyFrame(None,wx.ID_ANY,"")
    frame.Show()
    app.MainLoop() 