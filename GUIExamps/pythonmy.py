#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.8.9
# In conjunction with Tcl version 8.6
#    Mar 01, 2017 10:08:38 PM
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

import pythonmy_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel_1 (root)
    pythonmy_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel_1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel_1 (w)
    pythonmy_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None


class New_Toplevel_1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("605x454")
        top.title("New Toplevel 1")
        top.configure(highlightcolor="black")



        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.bilah_utama = Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.bilah_utama,
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Bilah utama")
        self.bilah_utama.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                command=pythonmy_support.# TODO,
                font="TkMenuFont",
                foreground="#000000",
                label="Keluar/Exit")


        self.TFrame1 = ttk.Frame(top)
        self.TFrame1.place(relx=0.02, rely=0.02, relheight=0.96, relwidth=0.97)
        self.TFrame1.configure(relief=GROOVE)
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief=GROOVE)
        self.TFrame1.configure(width=585)

        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.TNotebook1 = ttk.Notebook(self.TFrame1)
        self.TNotebook1.place(relx=0.02, rely=0.01, relheight=0.97
                , relwidth=0.96)
        self.TNotebook1.configure(width=562)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_pg0 = ttk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_pg0, padding=3)
        self.TNotebook1.tab(0, text="Page 1",underline="-1",)
        self.TNotebook1_pg1 = ttk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_pg1, padding=3)
        self.TNotebook1.tab(1, text="Page 2",underline="-1",)

        self.TLabel1 = ttk.Label(self.TNotebook1_pg0)
        self.TLabel1.place(relx=0.04, rely=0.15, height=16, width=137)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(relief=FLAT)
        self.TLabel1.configure(text='''No Id''')
        self.TLabel1.configure(width=137)

        self.Message1 = Message(self.TNotebook1_pg0)
        self.Message1.place(relx=0.13, rely=0.03, relheight=0.05, relwidth=0.74)
        self.Message1.configure(text='''Formulir Pendaftaran''')
        self.Message1.configure(width=413)

        self.TLabel2 = ttk.Label(self.TNotebook1_pg0)
        self.TLabel2.place(relx=0.04, rely=0.2, height=16, width=75)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(relief=FLAT)
        self.TLabel2.configure(text='''Nama Siswa''')

        self.TLabel3 = ttk.Label(self.TNotebook1_pg0)
        self.TLabel3.place(relx=0.04, rely=0.25, height=16, width=104)
        self.TLabel3.configure(background="#d9d9d9")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(relief=FLAT)
        self.TLabel3.configure(text='''Tempat,Tgl Lahir''')






if __name__ == '__main__':
    vp_start_gui()



