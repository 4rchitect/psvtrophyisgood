import tkMessageBox
from Tkinter import *

import os

import ParseTRPTITLE
import ParseTRPTRNS
import VitaTime
import psvtrophyisgoodModTRP

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

def set_Tk_var():
    global year
    year = StringVar()
    global mounth
    mounth = StringVar()
    global day
    day = StringVar()
    global hour
    hour = StringVar()
    global minute
    minute = StringVar()
    global second
    second = StringVar()

def apply(trophyId,npCommId,year,month,day,hour,minute,second):
    month = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November","December" ].index(month) + 1
    try:
        timestamp = VitaTime.encodeTimestamp("{}-{}-{} {}:{}:{}.{}".format(year,month,day,hour,minute,second,0))
    except:
        tkMessageBox.showerror(title="THAT MAKES NO SENSE!",message="You entered an impossible time.")
    ParseTRPTRNS.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/data/"+npCommId+"/TRPTRANS.DAT")
    ParseTRPTITLE.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/data/"+npCommId+"/TRPTITLE.DAT")
    ParseTRPTRNS.writeTimestamp(ParseTRPTRNS.findDataBlockForTrophy(trophyId),timestamp)
    ParseTRPTITLE.writeTimestamp(trophyId, timestamp)

    global lastTime
    lastTime = timestamp

    destroy_window()
    psvtrophyisgoodModTRP.vp_start_gui(npCommId)
    sys.stdout.flush()

def getLastTime():
    return lastTime

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
    import psvtrophyisgoodDateTime
    psvtrophyisgoodDateTime.vp_start_gui()


