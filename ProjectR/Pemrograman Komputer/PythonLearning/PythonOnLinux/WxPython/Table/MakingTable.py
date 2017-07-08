import wx
import wx.grid

class GridFrame(wx.Frame):

    def __init__(self, parent):

        wx.Frame.__init__(self, parent)
        GridNameStr = "Hello"
        # Create a wxGrid object
        grid = wx.grid.Grid(self, id=0, pos=wx.DefaultPosition, size=wx.DefaultSize,
        style=wx.WANTS_CHARS, name=GridNameStr)

        # Then we call CreateGrid to set the dimensions of the grid
        # (100 rows and 10 columns in this example)
        grid.CreateGrid(5, 10)

        # We can set the sizes of individual rows and columns
        # in pixels
        grid.SetRowSize(0,25)
        grid.SetColSize(0,80)

        # We want to set a label on Col
        grid.SetColLabelValue(0,"KodeTrx")
        grid.SetColLabelValue(1,"KodeBarang")


        # Insert data into tabel

        grid.SetCellValue(0,2,"Masuk Nggak")
        # And set grid cell contents as strings
        grid.SetCellValue(0, 0, 'Hallo')

        # We can specify that some cells are read.only
        grid.SetCellValue(0, 3, 'This is read.only')
        grid.SetReadOnly(0, 3)
        grid.EnableEditing(True)

        # Colours can be specified for grid cell contents
        grid.SetCellValue(3, 3, 'green on grey')
        grid.SetCellTextColour(3, 3, wx.GREEN)
        grid.SetCellBackgroundColour(3, 3, wx.LIGHT_GREY)

        # We can specify the some cells will store numeric
        # values rather than strings. Here we set grid column 5
        # to hold floating point values displayed with width of 6
        # and precision of 2
        grid.SetColFormatFloat(5, 6, 2)
        grid.SetCellValue(0, 6, '3.1415')

        self.Show()


if __name__ == '__main__':

    app = wx.App(0)
    frame = GridFrame(None)
    app.MainLoop()
