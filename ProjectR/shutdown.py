# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  4 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		
		fgSizer3 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		self.m_panel5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		
		gSizer4 = wx.GridSizer( 1, 2, 0, 0 )
		
		self.m_staticText3 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"No Komputer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		self.m_staticText3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		
		gSizer4.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		m_choice1Choices = [ u"Operator", u"Klien2", u"Klien3", u"Klien4", u"Klien5", u"Klien6", u"Klien7" ]
		self.m_choice1 = wx.Choice( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 1 )
		self.m_choice1.SetBackgroundColour( wx.Colour( 74, 137, 189 ) )
		
		gSizer4.Add( self.m_choice1, 0, wx.ALL, 5 )
		
		
		self.m_panel5.SetSizer( gSizer4 )
		self.m_panel5.Layout()
		gSizer4.Fit( self.m_panel5 )
		fgSizer3.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel6.SetForegroundColour( wx.Colour( 67, 19, 19 ) )
		self.m_panel6.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		
		gSizer2 = wx.GridSizer( 2, 2, 0, 0 )
		
		self.m_button1 = wx.Button( self.m_panel6, wx.ID_ANY, u"Shutdown", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_button1, 0, wx.ALL, 5 )
		
		self.m_button2 = wx.Button( self.m_panel6, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_button2, 0, wx.ALL, 5 )
		
		self.m_button3 = wx.Button( self.m_panel6, wx.ID_ANY, u"Reboot", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_button3, 0, wx.ALL, 5 )
		
		
		self.m_panel6.SetSizer( gSizer2 )
		self.m_panel6.Layout()
		gSizer2.Fit( self.m_panel6 )
		fgSizer3.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( fgSizer3 )
		self.Layout()
		fgSizer3.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_choice1.Bind( wx.EVT_CHOICE, self.pilihkomputer )
		self.m_button1.Bind( wx.EVT_BUTTON, self.Shutdown )
		self.m_button2.Bind( wx.EVT_BUTTON, self.Cancel )
		self.m_button3.Bind( wx.EVT_BUTTON, self.Reboot )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def pilihkomputer( self, event ):
		event.Skip()
	
	def Shutdown( self, event ):
		event.Skip()
	
	def Cancel( self, event ):
		event.Skip()
	
	def Reboot( self, event ):
		event.Skip()
	

