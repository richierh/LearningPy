#simple adding button to a frame

import wx

class Jendela(wx.Frame):

 def __init__(self,parent,id):
  MainWindow = wx.Frame.__init__(self,parent,id,pos=(300,40),size=(480,550),title="Hallo")
  panel = wx.Panel(self)
  button = wx.Button(self,pos=(100,100),size=wx.DefaultSize,label="Exit")
  button2 = wx.Button(self,label = "Halo Dunia",pos =(100,140),size=(100,50))


#This is code to call the ode
if __name__ == '__main__':
 Design = wx.App()
 BukaJendela = Jendela(parent = None,id=-1)
 BukaJendela.Show()
 Design.MainLoop()
