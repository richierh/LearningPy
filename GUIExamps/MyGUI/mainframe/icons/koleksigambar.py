import wx

class lokasigambar(wx.StaticBitmap,wx.Bitmap):
    """
    kode file Tempat naruh gambar icons
    """
    def __init__(self,*args,**kwds):
        super(lokasigambar,self).__init__(*args,**kwds)        
        self.Bitmap=wx.Bitmap(u"/home/pmc/mygit/LearningPy/GUIExamps/MyGUI/mainframe/icons/store.png",wx.BITMAP_TYPE_ANY)
        """disini sudah bisa """
    
    
    def __repr__(self):
        return print ("this is my functions")


