import wx
import mainframe.menu_utama


class FFormEvent(mainframe.menu_utama.FForm):
	"""
	"""

	def __init__(self, *args, **kwds):
		super(FFormEvent, self).__init__(*args, **kwds)

	def m_textCtrl1OnText(self, event):
		print (self.m_textCtrl1.GetValue())
		event.Skip()
	
	def m_textCtrl1OnText( self, event ):
		event.Skip()
	
	def	m_textCtrl2OnText( self, event ):
		event.Skip()
	
	def m_textCtrl3OnText( self, event ):
		event.Skip()
	
	def m_textCtrl4OnText( self, event ):
		event.Skip()
	
	def m_textCtrl5OnText( self, event ):
		event.Skip()
	
	def m_textCtrl6OnText( self, event ):
		event.Skip()
	
	def m_button1OnButtonClick( self, event ):
		event.Skip()
	
	def m_button2OnButtonClick( self, event ):
		print (self.m_textCtrl1.GetValue())
		print (self.m_textCtrl2.GetValue())
		print (self.m_textCtrl3.GetValue())
		print (self.m_textCtrl4.GetValue())
		print (self.m_textCtrl5.GetValue())
		print (self.m_textCtrl6.GetValue())
		print ("okay")
		event.Skip()
	
