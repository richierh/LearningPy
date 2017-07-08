import wx
import wx.wizard
 
########################################################################
class HalamanJudul(wx.wizard.WizardPageSimple):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self,parent,title):
        
        super(HalamanJudul,self).__init__(parent)
        
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.sizer)
 
        self.title = wx.StaticText(self, -1, title)
        self.title.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        self.sizer.Add(self.title, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        self.sizer.Add(wx.StaticLine(self, -1), 0, wx.EXPAND|wx.ALL, 5)
 
#----------------------------------------------------------------------
    
class main(wx.wizard.Wizard):
    def __init__(self,*args,**kwargs):
        
        """"""
        super(main,self).__init__(*args,**kwargs)
        #self.wizard = wx.wizard.Wizard(None, -1, "Grup Alumni 233 ")
        self.hal1 = HalamanJudul(self, "Grup ini hebat")
        self.hal2 = HalamanJudul(self, "Beda dari yang lainnya")
        self.hal3 = HalamanJudul(self, "Orangnya keren-keren")
        self.hal4 = HalamanJudul(self, "Apalagi yang namanya Richie")
     
        wx.wizard.WizardPageSimple.Chain(self.hal1,self.hal2)
        wx.wizard.WizardPageSimple.Chain(self.hal2,self.hal3)
        wx.wizard.WizardPageSimple.Chain(self.hal3,self.hal4)
        self.FitToPage(self.hal1)
     
        self.RunWizard(self.hal1)
     
        self.Destroy()
     
#----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.App()
    Rangka = main(None,title = "Grup Hebat")
    Rangka.Show()
    app.MainLoop()