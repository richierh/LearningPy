#!/usr/bin/env python
# spreadsheet.py

import wx
from wx.lib import sheet


class MySheet(sheet.CSheet):
    def __init__(self, parent):
        sheet.CSheet.__init__(self, parent)
        self.row = self.col = 0
        self.SetNumberRows(100000)
        self.SetNumberCols(25)
        

        for i in range(55):
            self.SetRowSize(i, 20)
        self.Bind(self,self.OnGridSelectCell,1)

    def OnGridSelectCell(self, event):
        self.row, self.col = event.GetRow(3), event.GetCol(2)
        control = self.GetParent().GetParent().position
        value =  self.GetColLabelValue(self.col) + self.GetRowLabelValue(self.row)
        control.SetValue(value)
        event.Skip()

class MyFrame(wx.Frame):

    def __init__(self,*args,**kwargs):
        super(MyFrame,self).__init__(*args,**kwargs)
        self.SetTitle("Hallo")
        
        box1 = wx.BoxSizer(wx.VERTICAL)
        self.panel = wx.Panel(self,-1)
        self.sheet1=MySheet(self)
        box1.Add(self.sheet1,1)
        self.SetSizer(box1)
        self.Layout()
      
        

if __name__=="__main__":
    app =  wx.App(True)
    frame = MyFrame(None,wx.ID_ANY,"")
    frame.Show()
    app.MainLoop() 