
import os
# import ParseTRPDB Fuck trophy_local.db >_>
import ParseTRPTITLE
import ParseTRPSFM
import ParseTRPTRNS
from Tkinter import *

import VitaTime

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import psvtrophyisgoodModTRP_support

def vp_start_gui(v):
    '''Starting point when module is the main routine.'''
    global npCommId
    npCommId = v
    global val, w, root
    root = Tk()
    root.protocol("WM_DELETE_WINDOW", lambda: os._exit(0))
    root.resizable(0, 0)
    top = modTRP (root)
    psvtrophyisgoodModTRP_support.init(root, top)
    root.mainloop()

w = None
def create_modTRP(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = modTRP (w)
    psvtrophyisgoodModTRP_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_modTRP():
    global w
    w.destroy()
    w = None


class modTRP:
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
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+435+122")
        top.title("psvtrophyisgood")



        self.Labelframe1 = LabelFrame(top)
        self.Labelframe1.place(relx=0.02, rely=0.0, relheight=0.99
                , relwidth=0.65)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(text='''Trophies''')
        self.Labelframe1.configure(width=390)

        self.trophySelection = ScrolledListBox(self.Labelframe1)
        self.trophySelection.place(relx=0.0, rely=0.0, relheight=0.99
                , relwidth=0.99)
        self.trophySelection.configure(background="white")
        self.trophySelection.configure(font="TkFixedFont")
        self.trophySelection.configure(highlightcolor="#d9d9d9")
        self.trophySelection.configure(selectbackground="#c4c4c4")
        self.trophySelection.configure(width=10)
        ParseTRPTRNS.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/data/"+npCommId+"/TRPTRANS.DAT")
        ParseTRPSFM.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/conf/"+npCommId+"/TROP.SFM")
        ParseTRPTITLE.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/data/"+npCommId+"/TRPTITLE.DAT")
        a = 0
        trophyList = ParseTRPSFM.getAllTrophies()
        numTrophys = ParseTRPSFM.getNumberOfTrophies()

        while a != numTrophys:
            ti = trophyList[a]
            if ParseTRPTRNS.findDataBlockForTrophy(a) == -1:
                tp = {"unlocked":False,"timestamp":["00000000000000","00000000000000"]}
            else:
                tp = ParseTRPTRNS.parseTrophyDataBlock(ParseTRPTRNS.findDataBlockForTrophy(a))

            tt = ParseTRPTITLE.parseDataBlock(a)
            if tt["unlocked"] or tp["unlocked"]:
                isUnlocked = True
            else:
                isUnlocked = False
            if isUnlocked == True:
                isUnlocked = "U"
            else:
                isUnlocked = "L"
            if isUnlocked == "U":
                if int(tp["timestamp"][0],16) >= 63082280000000000:
                    timestamp = "-"+str(VitaTime.decodeTimestamp(tp["timestamp"][0]))
                elif int(tt["timestamp"],16) >= 63082280000000000 and tt["unlocked"]:
                    timestamp = "-" + str(VitaTime.decodeTimestamp(tt["timestamp"]))
                else:
                    timestamp = "-NaN"
            else:
                timestamp = ""


            text = "("+str(a)+") "+ti["name"]+"-"+ti["grade"]+"-" + isUnlocked + str(timestamp)
            self.trophySelection.insert(a,text)
            a += 1

        self.Labelframe2 = LabelFrame(top)
        self.Labelframe2.place(relx=0.67, rely=0.0, relheight=0.48
                , relwidth=0.33)
        self.Labelframe2.configure(relief=GROOVE)
        self.Labelframe2.configure(text='''Options''')
        self.Labelframe2.configure(width=200)

        self.Labelframe3 = LabelFrame(self.Labelframe2)
        self.Labelframe3.place(relx=0.05, rely=0.09, relheight=0.4, relwidth=0.9)

        self.Labelframe3.configure(relief=GROOVE)
        self.Labelframe3.configure(text='''Timestamp''')
        self.Labelframe3.configure(width=180)

        self.changeStamp = Button(self.Labelframe3)
        self.changeStamp.place(relx=0.0, rely=0.0, height=26, width=170)
        self.changeStamp.configure(activebackground="#d9d9d9")
        self.changeStamp.configure(command=lambda: psvtrophyisgoodModTRP_support.cngStamp(npCommId,self.trophySelection.get(ACTIVE)))
        self.changeStamp.configure(text='''Change''')
        self.changeStamp.configure(width=170)

        self.randomStamp = Button(self.Labelframe3)
        self.randomStamp.place(relx=0.0, rely=0.47, height=26, width=130)
        self.randomStamp.configure(activebackground="#d9d9d9")
        self.randomStamp.configure(command=lambda: psvtrophyisgoodModTRP_support.rngStamp(npCommId,self.trophySelection.get(ACTIVE)))
        self.randomStamp.configure(text='''Random''')
        self.randomStamp.configure(width=130)

        self.RandomALL = Button(self.Labelframe3)
        self.RandomALL.place(relx=0.78, rely=0.47, height=27, width=37)
        self.RandomALL.configure(activebackground="#d9d9d9")
        self.RandomALL.configure(command=lambda: psvtrophyisgoodModTRP_support.randomAll(npCommId))
        self.RandomALL.configure(text='''ALL''')
        self.RandomALL.configure(width=37)


        self.Labelframe4 = LabelFrame(self.Labelframe2)
        self.Labelframe4.place(relx=0.05, rely=0.51, relheight=0.4, relwidth=0.9)
        self.Labelframe4.configure(relief=GROOVE)
        self.Labelframe4.configure(text='''State''')
        self.Labelframe4.configure(width=180)

        self.unlock = Button(self.Labelframe4)
        self.unlock.place(relx=0.0, rely=0.0, height=26, width=130)
        self.unlock.configure(activebackground="#d9d9d9")
        self.unlock.configure(command=lambda: psvtrophyisgoodModTRP_support.unlockTrophy(npCommId,self.trophySelection.get(ACTIVE)))
        self.unlock.configure(text='''Unlock''')
        self.unlock.configure(width=130)

        self.unlockALL = Button(self.Labelframe4)
        self.unlockALL.place(relx=0.78, rely=0.0, height=27, width=37)
        self.unlockALL.configure(activebackground="#d9d9d9")
        self.unlockALL.configure(command=lambda: psvtrophyisgoodModTRP_support.unlockAll(npCommId))
        self.unlockALL.configure(text='''ALL''')
        self.unlockALL.configure(width=37)

        self.lock = Button(self.Labelframe4)
        self.lock.place(relx=0.0, rely=0.47, height=26, width=130)
        self.lock.configure(activebackground="#d9d9d9")
        self.lock.configure(command=lambda: psvtrophyisgoodModTRP_support.lockTrophy(npCommId,self.trophySelection.get(ACTIVE)))
        self.lock.configure(text='''Lock''')
        self.lock.configure(width=130)

        self.lockAll = Button(self.Labelframe4)
        self.lockAll.place(relx=0.78, rely=0.47, height=27, width=37)
        self.lockAll.configure(activebackground="#d9d9d9")
        self.lockAll.configure(command=lambda: psvtrophyisgoodModTRP_support.lockALL(npCommId))
        self.lockAll.configure(text='''ALL''')
        self.lockAll.configure(width=37)

        self.Labelframe5 = LabelFrame(top)
        self.Labelframe5.place(relx=0.67, rely=0.49, relheight=0.41
                , relwidth=0.33)
        self.Labelframe5.configure(relief=GROOVE)
        self.Labelframe5.configure(text='''Global Options''')
        self.Labelframe5.configure(cursor="fleur")
        self.Labelframe5.configure(width=200)

        self.Labelframe6 = LabelFrame(self.Labelframe5)
        self.Labelframe6.place(relx=0.05, rely=0.11, relheight=0.46
                , relwidth=0.9)
        self.Labelframe6.configure(relief=GROOVE)
        self.Labelframe6.configure(text='''Accounts''')
        self.Labelframe6.configure(width=180)

        self.chgOwner = Button(self.Labelframe6)
        self.chgOwner.place(relx=0.0, rely=0.0, height=26, width=170)
        self.chgOwner.configure(activebackground="#d9d9d9")
        self.chgOwner.configure(command=lambda: psvtrophyisgoodModTRP_support.cngOwner(npCommId))
        self.chgOwner.configure(text='''Change Owner''')
        self.chgOwner.configure(width=170)

        self.rmOwner = Button(self.Labelframe6)
        self.rmOwner.place(relx=0.0, rely=0.47, height=26, width=170)
        self.rmOwner.configure(activebackground="#d9d9d9")
        self.rmOwner.configure(command=lambda: psvtrophyisgoodModTRP_support.rmOwner(npCommId))
        self.rmOwner.configure(text='''Remove Owner''')
        self.rmOwner.configure(width=167)

        self.Labelframe7 = LabelFrame(self.Labelframe5)
        self.Labelframe7.place(relx=0.05, rely=0.59, relheight=0.3, relwidth=0.9)

        self.Labelframe7.configure(relief=GROOVE)
        self.Labelframe7.configure(text='''Misc''')
        self.Labelframe7.configure(width=180)

        self.commSign = Button(self.Labelframe7)
        self.commSign.place(relx=0.0, rely=0.0, height=26, width=170)
        self.commSign.configure(activebackground="#d9d9d9")
        self.commSign.configure(command=lambda: psvtrophyisgoodModTRP_support.npCommSig(npCommId))
        self.commSign.configure(text='''Get NpCommSign''')
        self.commSign.configure(width=167)

        self.Back = Button(top)
        self.Back.place(relx=0.68, rely=0.91, height=26, width=188)
        self.Back.configure(activebackground="#d9d9d9")
        self.Back.configure(command=psvtrophyisgoodModTRP_support.back)
        self.Back.configure(text='''Back''')
        self.Back.configure(width=180)





# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = Pack.__dict__.keys() | Grid.__dict__.keys() \
                  | Place.__dict__.keys()
        else:
            methods = Pack.__dict__.keys() + Grid.__dict__.keys() \
                  + Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, Listbox):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

if __name__ == '__main__':
    vp_start_gui()



