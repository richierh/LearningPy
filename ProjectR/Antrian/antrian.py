import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import antrian_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Antriy (root)
    antrian_support.init(root, top)
    root.mainloop()

w = None
def create_Antriy(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Antriy (w)
    antrian_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Antriy():
    global w
    w.destroy()
    w = None


class Antriy:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font10 = "-family {DejaVu Sans} -size 30 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.resizable(height =  False,width = False)
        top.geometry("599x430+385+181")
        top.title("Antriy")
        top.configure(highlightcolor="black")



        self.TFrame1 = ttk.Frame(top)
        self.TFrame1.place(relx=0.01, rely=0.01, relheight=0.95, relwidth=0.98)
        self.TFrame1.configure(relief=GROOVE)
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief=GROOVE)
        self.TFrame1.configure(width=588)

        self.TLabel1 = ttk.Label(self.TFrame1)
        self.TLabel1.place(relx=0.02, rely=0.02, height=107, width=567)
        self.TLabel1.configure(background="#ffffbb")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font=font10)
        self.TLabel1.configure(relief=FLAT)
        self.TLabel1.configure(anchor=CENTER)
        self.TLabel1.configure(justify=CENTER)
        self.TLabel1.configure(text='''NO 51''')

        self.TButton1 = ttk.Button(self.TFrame1)
        self.TButton1.place(relx=0.02, rely=0.32, height=266, width=343)
        self.TButton1.configure(command=antrian_support.Tekan)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''TEKAN''')

        self.TButton2 = ttk.Button(self.TFrame1)
        self.TButton2.place(relx=0.63, rely=0.32, height=196, width=203)
        self.TButton2.configure(command=antrian_support.Refresh)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''REFRESH''')

        self.Message1 = Message(self.TFrame1)
        self.Message1.place(relx=0.63, rely=0.81, relheight=0.15, relwidth=0.33)
        self.Message1.configure(font=font10)
        self.Message1.configure(text='''ID : 03''')
        self.Message1.configure(width=195)






if __name__ == '__main__':
    vp_start_gui()



