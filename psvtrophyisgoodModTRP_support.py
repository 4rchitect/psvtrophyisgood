import Tkinter
import json
import tkMessageBox


import os
import tkSimpleDialog

import datetime
import requests
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
    ParseTRPTITLE.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/data/" + npCommId + "/TRPTITLE.DAT")
    ParseTRPTRNS.init(os.path.dirname(os.path.realpath(__file__)) + "/trophyDownloaded/data/" + npCommId + "/TRPTRANS.DAT")
    if ParseTRPTRNS.findDataBlockForTrophy(trophyId) == -1:
        ParseTRPTRNS.unlockTrophy(trophyId)
        ParseTRPTRNS.init(os.path.dirname(os.path.realpath(__file__)) + "/trophyDownloaded/data/" + npCommId + "/TRPTRANS.DAT")
        ## Program could crash when trying to lock a trophy found in TRPTITLE but not TRPTRANS.
        ## This fixes that.
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

        if ParseTRPTRNS.findDataBlockForTrophy(trophyId) == -1:
            ParseTRPTRNS.unlockTrophy(trophyId)
            ParseTRPTRNS.init(os.path.dirname(os.path.realpath(__file__)) + "/trophyDownloaded/data/" + npCommId + "/TRPTRANS.DAT")
            ## Program could crash when trying to lock a trophy found in TRPTITLE but not TRPTRANS.
            ## This fixes that.

        ParseTRPTRNS.lockTrophy(trophyId,True)
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

def stealFromPsn(npCommId):
    destroy_window()

    window = Tkinter.Tk()
    window.wm_withdraw()


    userInfoCookie = ""
    ##Throwaway account i dont care about ^

    onlineId = tkSimpleDialog.askstring(title="Trophy Stealer",prompt="Enter a PSN Username of someone who has this trophy set.")
    if onlineId == None:
        window.destroy()
        psvtrophyisgoodModTRP.vp_start_gui(npCommId)

    headers = {"Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Encoding": "zip, deflate, br","Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", "Connection": "keep-alive","Host": "io.playstation.com", "Origin": "https://www.playstation.com","Referer": "https://www.playstation.com/en-ca/my/compare-game-trophies/","User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/64.0.3282.167 Chrome/64.0.3282.167 Safari/537.36"}  ##So that where not saying "Hello im a bot!" to sony.
    url = "https://io.playstation.com/playstation/psn/profile/compareGames/trophies/data"
    params = (("gameId", npCommId), ("userIds", onlineId + "," + onlineId.lower()), ("userInfoCookie", userInfoCookie))
    try:
        print "Connecting to PSN..."
        trophyData = json.loads(requests.get(url=url, params=params, headers=headers).content)
    except:
        tkMessageBox.showerror(title="Connection Failed.",message="Could not contact server.")
        window.destroy()
        psvtrophyisgoodModTRP.vp_start_gui(npCommId)
        return -1
    try:
        trophyData = trophyData['users']
        trophyData = trophyData[0]
        trophyData = trophyData['list']
        if trophyData != []:
            print trophyData

            ## Lock all trophys

            ParseTRPSFM.init(os.path.dirname(os.path.realpath(__file__)) + "/trophyDownloaded/conf/" + npCommId + "/TROP.SFM")
            a = 0
            while a != ParseTRPSFM.getNumberOfTrophies():
                ParseTRPTRNS.init(os.path.dirname(
                    os.path.realpath(__file__)) + "/trophyDownloaded/data/" + npCommId + "/TRPTRANS.DAT")
                ParseTRPTITLE.init(os.path.dirname(
                    os.path.realpath(__file__)) + "/trophyDownloaded/data/" + npCommId + "/TRPTITLE.DAT")
                ParseTRPTITLE.lockTrophy(a)
                if ParseTRPTRNS.findDataBlockForTrophy(a) != -1:
                    ParseTRPTRNS.lockTrophy(a,True)
                a += 1

            ## Unlock Trophys

            a = 0
            ParseTRPSFM.init(os.path.dirname(os.path.realpath(__file__)) + "/trophyDownloaded/conf/" + npCommId + "/TROP.SFM")
            while a != ParseTRPSFM.getNumberOfTrophies():
                tropInfo = trophyData[a]
                if tropInfo['trophyWon'] != 0:
                    ParseTRPTRNS.init(os.path.dirname(os.path.realpath(__file__)) + "/trophyDownloaded/data/" + npCommId + "/TRPTRANS.DAT")
                    ParseTRPTITLE.init(os.path.dirname(os.path.realpath(__file__)) + "/trophyDownloaded/data/" + npCommId + "/TRPTITLE.DAT")
                    ParseTRPTITLE.unlockTrophy(a)
                    ParseTRPTRNS.unlockTrophy(a)

                    ## Write timestamps
                    unlockDate = datetime.datetime.strptime(tropInfo['trophyStamp'], "%Y-%m-%dT%H:%M:%SZ")
                    unlockDate = str(unlockDate)
                    timestamp = VitaTime.encodeTimestamp(unlockDate + ".00")
                    ParseTRPTRNS.init(os.path.dirname(os.path.realpath(__file__)) + "/trophyDownloaded/data/" + npCommId + "/TRPTRANS.DAT")
                    ParseTRPTITLE.init(os.path.dirname(os.path.realpath(__file__)) + "/trophyDownloaded/data/" + npCommId + "/TRPTITLE.DAT")
                    print ParseTRPTRNS.findDataBlockForTrophy(a)
                    ParseTRPTRNS.writeTimestamp(ParseTRPTRNS.findDataBlockForTrophy(a), timestamp)
                    print a
                    ParseTRPTITLE.writeTimestamp(a, timestamp)

                a += 1

        else:
            tkMessageBox.showerror(title="Trophy Set Not Found", message="The user you specified does not have this trophy set.")
    except:
        tkMessageBox.showerror(title="Trophy Set Not Found",message="The user you specified does not have this trophy set.")
    window.destroy()

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



