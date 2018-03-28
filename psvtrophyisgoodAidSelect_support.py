from Tkinter import *
import ttk

import ParseTRPTITLE
import ParseTRPTRNS
import psvtrophyisgoodModTRP


def set_Tk_var():
    global byte1
    byte1 = StringVar()
    global byte2
    byte2 = StringVar()
    global byte3
    byte3 = StringVar()
    global byte4
    byte4 = StringVar()
    global byte5
    byte5 = StringVar()
    global byte6
    byte6 = StringVar()
    global byte7
    byte7 = StringVar()
    global byte8
    byte8 = StringVar()

def apply(npCommId,byte1,byte2,byte3,byte4,byte5,byte6,byte7,byte8):
    destroy_window()
    aid = byte1+byte2+byte3+byte4+byte5+byte6+byte7+byte8
    ParseTRPTRNS.init("data/"+npCommId+"/TRPTRANS.DAT")
    ParseTRPTITLE.init("data/"+npCommId+"/TRPTITLE.DAT")
    ParseTRPTRNS.setAccountId(aid)
    ParseTRPTITLE.setAccountId(aid)
    psvtrophyisgoodModTRP.vp_start_gui(npCommId)



def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import psvtrophyisgoodAidSelect
    psvtrophyisgoodAidSelect.vp_start_gui()


