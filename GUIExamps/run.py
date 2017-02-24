from MainFrame import *
import wx


if __name__ == '__main__':
    root = wx.App(True)
    Frame = MyFrame(None)
    Frame.Show(True)
    root.MainLoop()
