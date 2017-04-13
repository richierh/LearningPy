import wx

print ("hello world")
class Frame(wx.Frame) :
	def __init__(self,title):
		wx.Frame.__init__(self,None,title=title,size= (300,300))
app = wx.App(redirect=True)
top = Frame("Hello")
top.Show()
app.Mainloop()
