import wx

class MyFrame(wx.Frame):
 def __init__(self, *args, **kwds):
# begin wxGlade: MyFrame.__init__#
  kwds["style"] = wx.DEFAULT_FRAME_STYLE
  wx.Frame.__init__(self, *args, **kwds)
  self.label_1 = wx.StaticText(self, -1, "Coba", style=wx.ALIGN_CENTRE)
  self.button_1 = wx.Button(self, -1, "Click me!")

  self.__set_properties()
  self.__do_layout()

  self.Bind(wx.EVT_BUTTON, self.Btn1Click, self.button_1)
# end wxGlade

def __set_properties(self):
# begin wxGlade: MyFrame.__set_properties
  self.SetTitle("frame_1")
# end wxGlade

def __do_layout(self):
# begin wxGlade: MyFrame.__do_layout
 sizer_1 = wx.BoxSizer(wx.VERTICAL)
 sizer_1.Add((20, 40), 0, 0, 0)
 sizer_1.Add(self.label_1, 0, wx.EXPAND, 2)
 sizer_1.Add((40, 40), 0, 0, 0)
 sizer_1.Add(self.button_1, 0, 0, 0)
 self.SetSizer(sizer_1)
 sizer_1.Fit(self)
 self.Layout()
# end wxGlade

def Btn1Click(self, event): # wxGlade: MyFrame.
 self.label_1.SetLabel("Hey! at last you found me!")
#event.Skip()

if __name__ == "__main__":
 app = wx.PySimpleApp(0)
 wx.InitAllImageHandlers()
 frame_1 = MyFrame(None, -1,"")
 app.SetTopWindow(frame_1)
 frame_1.Show()
 app.MainLoop()
