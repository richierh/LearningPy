import wx

class mainok(wx.Frame):

    def __init__(self,*args,**kwargs):
        super(mainok,self).__init__(None,**kwargs)
        self.title("je;l")
        pass


main =  wx.App()
mainok =  wx.Frame(None,title="hello")
mainok.Show()
main.MainLoop()
