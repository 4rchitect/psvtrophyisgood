

from Tkinter import *

import os

import PFS

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1


def npCommSign():
    print('psvtrophyisgoodSelectSet_support.npCommSign')
    sys.stdout.flush()

def selectSet(npCommId):
    print "Decrypting "+npCommId
    PFS.decryptPFS(os.getcwd()+"/data/"+npCommId)

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
    import psvtrophyisgoodSelectSet
    psvtrophyisgoodSelectSet.vp_start_gui()


