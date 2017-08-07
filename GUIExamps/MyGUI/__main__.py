#! /usr/bin/python
import wx
import gettext
import mainframe.form


class MyApp(wx.App):
    def OnInit(self):
        self.frame = mainframe.form.MyFrame1(None)
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True


if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name
    app = MyApp(0)
    app.MainLoop()