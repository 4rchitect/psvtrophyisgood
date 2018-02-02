


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


def back():
    print('psvtrophyisgoodModTRP_support.back')
    sys.stdout.flush()

def cngOwner():
    print('psvtrophyisgoodModTRP_support.cngOwner')
    sys.stdout.flush()

def cngStamp():
    print('psvtrophyisgoodModTRP_support.cngStamp')
    sys.stdout.flush()

def lockTrophy():
    print('psvtrophyisgoodModTRP_support.lockTrophy')
    sys.stdout.flush()

def npCommSig():
    print('psvtrophyisgoodModTRP_support.npCommSig')
    sys.stdout.flush()

def rmOwner():
    print('psvtrophyisgoodModTRP_support.rmOwner')
    sys.stdout.flush()

def rngStamp():
    print('psvtrophyisgoodModTRP_support.rngStamp')
    sys.stdout.flush()

def unlockTrophy():
    print('psvtrophyisgoodModTRP_support.unlockTrophy')
    sys.stdout.flush()

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
    import psvtrophyisgoodModTRP
    psvtrophyisgoodModTRP.vp_start_gui()


