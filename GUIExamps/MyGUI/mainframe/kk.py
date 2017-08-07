import wx

class size(wx.Frame):
    def __init__(self,*args,**kwds):
        super(size,self).__init__(*args,**kwds)
        self.SetSizeHints( wx.Size( 500,300 ), wx.DefaultSize )
        print ("hello")