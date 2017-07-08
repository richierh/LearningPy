# /usr/bin/python
import wx

class mymainframe(wx.Frame):
    def __init__(self,*args,**kwargs):
        super(mymainframe,self).__init__(*args,**kwargs)
        self.boxsizer = wx.BoxSizer
        self.Move((800,800))
        self.Show()


root = wx.App(False)
joe = mymainframe(None,title="hello")
#joe.Show()
root.MainLoop()