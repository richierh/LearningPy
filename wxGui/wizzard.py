#!usr/bin/env python
import wx
import wx.wizard

class Jendela_Wizzard ( wx.wizard.Wizard ):
	
	def __init__( self, parent ):
		wx.wizard.Wizard.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, bitmap = wx.NullBitmap, pos = wx.DefaultPosition, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.Halaman = []
		
		self.m_wizPage1 = wx.wizard.WizardPageSimple( self  )
		self.tambah_hal( self.m_wizPage1 )
		
		self.m_wizPage2 = wx.wizard.WizardPageSimple( self  )
		self.tambah_hal( self.m_wizPage2 )
		
		self.Centre( wx.BOTH )
		
	def tambah_hal(self, page):
		if self.Halaman:
			previous_page = self.Halaman[-1]
			page.SetPrev(previous_page)
			previous_page.SetNext(page)
		self.Halaman.append(page)
	
	def __del__( self ):
		pass
	


if __name__=="__main__":
	main =  wx.App()
	frame = Jendela_Wizzard(None)
	frame.Show()
	main.MainLoop()

