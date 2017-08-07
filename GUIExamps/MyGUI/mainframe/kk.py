import wx

class size(wx.Frame):
    def __init__(self,*args,**kwds):
        super(size,self).__init__(*args,**kwds)
<<<<<<< HEAD
        print ("hello")
        self.aku = ""
=======
        self.SetSizeHints( wx.Size( 500,300 ), wx.DefaultSize )
        print ("hello")
>>>>>>> c46a7ef7a5d8c56b25c9726b641223b46f9e4ec8
