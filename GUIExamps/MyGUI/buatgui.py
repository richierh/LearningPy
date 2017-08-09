#!/usr/bin/python


import wx

class rangka(wx.Frame):
    """
    """
    def __init__(self,*args,**kwds):
        super(rangka,self).__init__(*args,**kwds)
        self.boxsizer = wx.BoxSizer()
        self.boxsizer.Orientation = wx.HORIZONTAL
        self.boxsizer.SetOrientation(self.boxsizer.Orientation)
        print (self.boxsizer.GetOrientation())
        self.mypanel = wx.Panel(self,wx.ID_ANY,pos= wx.DefaultPosition)
        self.Colour = wx.Colour(0,0,0)
        self.mypanel.SetBackgroundColour(self.Colour)


root=wx.App()
f=rangka(None)
f.Show()
root.MainLoop()