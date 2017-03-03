"This is my first GUI design for python"
import wx

app = wx.App()
win = wx.Frame(None, title="Editor",pos=(200,200), size=(800, 335))
win.Show()

loadButton = wx.Button(win, label='Open',pos=(225, 5), size=(80, 25))
saveButton = wx.Button(win, label='Save',pos=(315, 5), size=(80, 25))

app.MainLoop()
