import tkMessageBox


import os

import ParseTRPSFM
import ParseTRPTITLE
import ParseTRPTRNS
import VitaTime
import psvtrophyisgoodAidSelect
import psvtrophyisgoodRandomTime
import psvtrophyisgoodRandomTime_support
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
    ParseTRPTRNS.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/data/"+npcommid+"/TRPTRANS.DAT")
    ParseTRPTITLE.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/data/"+npcommid+"/TRPTITLE.DAT")
    if ParseTRPTRNS.findDataBlockForTrophy(trophyid) != -1 or ParseTRPTITLE.parseDataBlock(trophyid)["unlocked"]:
        destroy_window()
        psvtrophyisgoodDateTime.vp_start_gui(npcommid,trophyid)
    else:
        tkMessageBox.showerror(title="Uhh..",message="You cant set a timestamp for a locked trophy!")





def lockTrophy(npCommId,trophy):
    destroy_window()
    trophyId = getTrophyId(trophy)
    ParseTRPTRNS.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/data/" + npCommId + "/TRPTRANS.DAT")
    ParseTRPTITLE.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/data/" + npCommId + "/TRPTITLE.DAT")
    ParseTRPTITLE.lockTrophy(trophyId)
    ParseTRPTRNS.lockTrophy(trophyId)
    psvtrophyisgoodModTRP.vp_start_gui(npCommId)

def lockALL(npCommId):
    ParseTRPSFM.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/conf/" + npCommId + "/TROP.SFM")
    numTrophys = ParseTRPSFM.getNumberOfTrophies()
    trophyId = 0
    while trophyId != numTrophys:
        ParseTRPTRNS.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/data/" + npCommId + "/TRPTRANS.DAT")
        ParseTRPTITLE.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/data/" + npCommId + "/TRPTITLE.DAT")
        ParseTRPTITLE.lockTrophy(trophyId)
        if ParseTRPTRNS.findDataBlockForTrophy(trophyId) != -1:
            ParseTRPTRNS.lockTrophy(trophyId)
        trophyId += 1
    destroy_window()
    psvtrophyisgoodModTRP.vp_start_gui(npCommId)


def npCommSig(npCommId):
    psvtrophyisgoodNpCommSign.vp_start_gui(npCommId)
    sys.stdout.flush()

def rmOwner(npCommId):
    ParseTRPTRNS.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/data/"+npCommId+"/TRPTRANS.DAT")
    ParseTRPTRNS.setAccountId("0000000000000000")
    ParseTRPTITLE.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/data/"+npCommId+"/TRPTITLE.DAT")
    ParseTRPTITLE.setAccountId("0000000000000000")
    tkMessageBox.showinfo(title="Yep Yep!",message="Done! This trophy set can now be used by anyone!")
    sys.stdout.flush()

def rngStamp(npCommId,trophy):
    destroy_window()
    trophyId = getTrophyId(trophy)

    psvtrophyisgoodRandomTime.vp_start_gui()
    timestamps = psvtrophyisgoodRandomTime_support.getTimestamps()
    timestamp = VitaTime.genRandomTime(timestamps[0],timestamps[1])

    ParseTRPTRNS.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/data/"+npCommId+"/TRPTRANS.DAT")
    ParseTRPTITLE.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/data/"+npCommId+"/TRPTITLE.DAT")
    if ParseTRPTITLE.parseDataBlock(trophyId)["unlocked"]:
        if ParseTRPTRNS.findDataBlockForTrophy(trophyId) == -1:
            ParseTRPTRNS.unlockTrophy(trophyId)
            ParseTRPTITLE.unlockTrophy(trophyId)
            ParseTRPTRNS.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/data/" + npCommId + "/TRPTRANS.DAT")
            ParseTRPTITLE.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/data/" + npCommId + "/TRPTITLE.DAT")
        ParseTRPTRNS.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/data/" + npCommId + "/TRPTRANS.DAT")
        ParseTRPTITLE.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/data/" + npCommId + "/TRPTITLE.DAT")
        ParseTRPTRNS.writeTimestamp(ParseTRPTRNS.findDataBlockForTrophy(trophyId), timestamp)
        ParseTRPTITLE.writeTimestamp(trophyId, timestamp)
    else:
        tkMessageBox.showerror(title="Uhh..",message="You cant set a timestamp for a locked trophy!")
    psvtrophyisgoodModTRP.vp_start_gui(npCommId)
    sys.stdout.flush()

def randomAll(npCommId):
    destroy_window()
    trophyId = 0
    ParseTRPSFM.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/conf/" + npCommId + "/TROP.SFM")
    ParseTRPTRNS.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/data/" + npCommId + "/TRPTRANS.DAT")
    ParseTRPTITLE.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/data/" + npCommId + "/TRPTITLE.DAT")
    numTrophys = ParseTRPSFM.getNumberOfTrophies()
    psvtrophyisgoodRandomTime.vp_start_gui()
    timestamps = psvtrophyisgoodRandomTime_support.getTimestamps()
    while trophyId != numTrophys:
        if ParseTRPTITLE.parseDataBlock(trophyId)["unlocked"]:
            if ParseTRPTRNS.findDataBlockForTrophy(trophyId) == -1:
                ParseTRPTRNS.unlockTrophy(trophyId)
                ParseTRPTITLE.unlockTrophy(trophyId)
                ParseTRPTRNS.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/data/" + npCommId + "/TRPTRANS.DAT")
                ParseTRPTITLE.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/data/" + npCommId + "/TRPTITLE.DAT")
            ParseTRPTRNS.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/data/" + npCommId + "/TRPTRANS.DAT")
            ParseTRPTITLE.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/data/" + npCommId + "/TRPTITLE.DAT")
            timestamp = VitaTime.genRandomTime(timestamps[0], timestamps[1])
            ParseTRPTRNS.writeTimestamp(ParseTRPTRNS.findDataBlockForTrophy(trophyId), timestamp)
            ParseTRPTITLE.writeTimestamp(trophyId, timestamp)
        trophyId += 1
    psvtrophyisgoodModTRP.vp_start_gui(npCommId)



def unlockTrophy(npCommId,trophy):
    destroy_window()
    trophyId = getTrophyId(trophy)
    ParseTRPTRNS.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/data/" + npCommId + "/TRPTRANS.DAT")
    ParseTRPTITLE.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/data/" + npCommId + "/TRPTITLE.DAT")
    ParseTRPTITLE.unlockTrophy(trophyId)
    ParseTRPTRNS.unlockTrophy(trophyId)
    psvtrophyisgoodModTRP.vp_start_gui(npCommId)

def unlockAll(npCommId):
    ParseTRPSFM.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/conf/" + npCommId + "/TROP.SFM")
    numTrophys = ParseTRPSFM.getNumberOfTrophies()
    trophyId = 0
    while trophyId != numTrophys:
        ParseTRPTRNS.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/data/" + npCommId + "/TRPTRANS.DAT")
        ParseTRPTITLE.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/data/" + npCommId + "/TRPTITLE.DAT")
        ParseTRPTITLE.unlockTrophy(trophyId)
        ParseTRPTRNS.unlockTrophy(trophyId)
        trophyId += 1
    destroy_window()
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



