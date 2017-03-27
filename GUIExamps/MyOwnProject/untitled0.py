#!usr/bin/env python
import wx

class MainF(wx.Frame):
    """
    """
    def __init__(self,parent):
        super(MainF,self).__init__(parent,title="Ini Judul")
        self.Centre(True)
        Panel1 = wx.Panel(self,wx.ID_ANY,parent)
        







if __name__=="__main__":
    root = wx.App()
    utama = MainF(None)
    utama.Show()
    root.MainLoop()


