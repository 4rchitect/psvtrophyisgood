import tkMessageBox

import time

import ParseTRPTRNS
import VitaTime
import psvtrophyisgoodAidSelect
import psvtrophyisgoodSelectSet
import psvtrophyisgoodDateTime
import psvtrophyisgoodModTRP
import psvtrophyisgoodNpCommSign
from Tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

def getTrophyId(trophy):
    a = trophy.index("(")+1
    trophyid = trophy[a:]
    b = trophy.index(")")-1
    trophyid = trophyid[:b]
    trophyid = int(trophyid)
    return trophyid
def back():
    destroy_window()
    psvtrophyisgoodSelectSet.vp_start_gui()
    sys.stdout.flush()

def cngOwner(npCommId):
    destroy_window()
    psvtrophyisgoodAidSelect.vp_start_gui(npCommId)
    sys.stdout.flush()

def cngStamp(npcommid,trophy):
    trophyid = getTrophyId(trophy)
    ParseTRPTRNS.init("data/"+npcommid+"_decrypted/TRPTRANS.DAT")
    if ParseTRPTRNS.parseTrophyDataBlock(trophyid)["unlocked"]:
        destroy_window()
        psvtrophyisgoodDateTime.vp_start_gui(npcommid,trophyid)
    else:
        tkMessageBox.showerror(title="Uhh..",message="You cant set a timestamp for a locked trophy!")


def lockTrophy(npCommId,trophy):
    destroy_window()
    trophyId = getTrophyId(trophy)
    ParseTRPTRNS.init("data/" + npCommId + "_decrypted/TRPTRANS.DAT")
    ParseTRPTRNS.lockTrophy(trophyId)
    psvtrophyisgoodModTRP.vp_start_gui(npCommId)

def npCommSig(npCommId):
    psvtrophyisgoodNpCommSign.vp_start_gui(npCommId)
    sys.stdout.flush()

def rmOwner(npCommId):
    ParseTRPTRNS.init("data/"+npCommId+"_decrypted/TRPTRANS.DAT")
    ParseTRPTRNS.setAccountId("0000000000000000")
    tkMessageBox.showinfo(title="Yep Yep!",message="Done! This trophy set can now be used by anyone!")
    sys.stdout.flush()

def rngStamp(npCommId,trophy):
    trophyId = getTrophyId(trophy)
    timestamp = VitaTime.genRandomTime()
    ParseTRPTRNS.init("data/"+npCommId+"_decrypted/TRPTRANS.DAT")
    if ParseTRPTRNS.parseTrophyDataBlock(trophyId)["unlocked"]:
        #There was some weird bug where invalid timestamps behaved strangly.
        #Simple fix: Make it not invalid then generate stamp
        if int(ParseTRPTRNS.parseTrophyDataBlock(trophyId)["timestamp"][0], 16) < 63082281600000000:
            ts = hex(int(63082281600000000))[2:]
            if ts.endswith("L"):
                ts = ts[:-1]
            ParseTRPTRNS.writeTimestamp(trophyId, ts)
            rngStamp(npCommId,trophy)

        ParseTRPTRNS.writeTimestamp(trophyId,timestamp)
        destroy_window()
        psvtrophyisgoodModTRP.vp_start_gui(npCommId)
    else:
        tkMessageBox.showerror(title="Uhh..",message="You cant set a timestamp for a locked trophy!")
    sys.stdout.flush()

def unlockTrophy(npCommId,trophy):
    destroy_window()
    trophyId = getTrophyId(trophy)
    ParseTRPTRNS.init("data/" + npCommId + "_decrypted/TRPTRANS.DAT")
    ParseTRPTRNS.unlockTrophy(trophyId)
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



