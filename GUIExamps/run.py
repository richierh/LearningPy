from MainFrame import *
import wx

class motherframe(MyFrame1):
    def __init__(self,parent):
        super(self,motherframe).__init__(None)
        self.frame = MyFrame1(None)
        self.frame.Show(True)


if __name__ == '__main__':
    root = wx.App(True)
    Frame = motherframe(None)
    root.MainLoop()
