import wx

class size(wx.Frame):
    def __init__(self,*args,**kwds):
        super(size,self).__init__(*args,**kwds)
        print ("hello")
        self.SetSizeHints( wx.Size( 500,300 ), wx.DefaultSize )
        print ("hello")
        self.aku()
    
    def aku(self):
        return print ("hallggo")
