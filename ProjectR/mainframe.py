"""Subclass of MyFrame1, which is generated by wxFormBuilder."""

import wx
import shutdown

# Implementing MyFrame1
class Shutdown( shutdown.MyFrame1 ):
	def __init__( self, parent ):
		shutdown.MyFrame1.__init__( self, parent )
	
	# Handlers for MyFrame1 events.
	def pilihkomputer( self, event ):
		# TODO: Implement pilihkomputer
		pass
	
	def Shutdown( self, event ):
		# TODO: Implement Shutdown
		pass
	
	def Cancel( self, event ):
		# TODO: Implement Cancel
		self.Close()
		pass
	
	def Reboot( self, event ):
		# TODO: Implement Reboot
		pass
	
	
if __name__=="__main__":
        app=wx.App(False)
        Frame = Shutdown(None)
        Frame.Show(True)
        app.MainLoop()
        
