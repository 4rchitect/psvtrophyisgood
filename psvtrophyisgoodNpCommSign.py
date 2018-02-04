
import ParseTRPTRNS


from Tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import psvtrophyisgoodNpCommSign_support

def vp_start_gui(v):
    global npCommId
    npCommId = v
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = psvtrophyisgood (root)
    psvtrophyisgoodNpCommSign_support.init(root, top)
    root.mainloop()

w = None
def create_psvtrophyisgood(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = psvtrophyisgood (w)
    psvtrophyisgoodNpCommSign_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_psvtrophyisgood():
    global w
    w.destroy()
    w = None


class psvtrophyisgood:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("351x105+388+201")
        top.title("psvtrophyisgood")



        self.npComSign = Text(top)
        self.npComSign.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.npComSign.configure(background="white")
        self.npComSign.configure(font="TkTextFont")
        self.npComSign.configure(selectbackground="#c4c4c4")
        self.npComSign.configure(width=460)
        self.npComSign.configure(wrap=WORD)
        ParseTRPTRNS.init("data/"+npCommId+"_decrypted/TRPTRANS.DAT")
        self.npComSign.insert(END,ParseTRPTRNS.getNpCommSign())







