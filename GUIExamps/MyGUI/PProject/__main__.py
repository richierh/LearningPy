#!usr/bin/python
import wx
from Module import *
from Module.gui import MyFrame 

#class MainFrame(gui.MyFrame):
#    def __init__(self,*args,**kwds):
#       super(MainFrame,self).__init__(*args,**kwds)
        
print ("hello")
if __name__=="__main__":
    root = wx.App()
    winframe = MyFrame(None)
    winframe.Show()
    root.MainLoop()
    
