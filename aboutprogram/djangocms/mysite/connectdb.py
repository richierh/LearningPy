from Tkinter import Tk




class frameku(Frame):
    # This is my Frame
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.button = Button(self,parent)
        self.parent = parent
        self.frame = frame(self,parent)
        print ("hello")
        pass
    def eventku(self,event):
        pass

if __name__=="__main__":
    form = Tk()
    test = frameku(form)
    form.title("ini punya saya")
    form.mainloop()
