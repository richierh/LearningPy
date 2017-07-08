import wx
Window = wx.App()
RangkaLuar = wx.Frame(None,1,title = "Hai",size = (150,250),pos=(500,250))
btn = wx.Button("hello")
btn.Show()
RangkaLuar.Show()
Window.MainLoop()