#!/usr/bin/python

# nominimizebox.py

import wx

app = wx.App()
window = wx.Frame(None,-1, title='', pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_FRAME_STYLE, name = "frame")
window.Show(True)

app.MainLoop()
