

import ftplib
import tkMessageBox
from ftplib import FTP
import tkSimpleDialog
import os

import sys

import ftpExt
import psvtrophyisgoodSelectSet


def getIP():
    import Tkinter
    window = Tkinter.Tk()
    window.wm_withdraw()
    serverIp = tkSimpleDialog.askstring("FTP Connection","Please enter FTP Mode on your PSVITA, and enter the IP Below:")
    window.destroy()
    return serverIp
serverIp = getIP()
if serverIp == None:
    os._exit(0)
if serverIp.endswith(":1337"):
    serverIp = serverIp[:-5]

if not os.path.exists("trophyDownloaded/db"):
    os.makedirs("trophyDownloaded/db")
if not os.path.exists("trophyDownloaded/data"):
    os.makedirs("trophyDownloaded/data")
if not os.path.exists("trophyDownloaded/conf"):
    os.makedirs("trophyDownloaded/conf")



print "Connecting to: "+serverIp
try:
    ftp = FTP()
    print ftp.connect(serverIp,1337)

    listing = []
    directorys = []

    print "Moving to ur0:/user/00/trophy/conf"
    print ftp.cwd("/ur0:/user/00/trophy/conf")
    ftp.retrlines("LIST",listing.append)
    owd = os.getcwd()
    os.chdir("trophyDownloaded/conf")
    print "ur0:/user/00/trophy/data/*"
    ftpExt.downloadRecursive(ftp)

    os.chdir(owd+"/trophyDownloaded/data")
    print ftp.cwd("/ux0:/reSync")
    print "Downloading /ux0:/reSync/*"
    ftpExt.downloadRecursive(ftp)
    print "Done!"
    global ftpDone
    #os.remove("data/TRPUSER.DAT")
    psvtrophyisgoodSelectSet.vp_start_gui()
except ftplib.error_perm:
    import Tkinter
    window = Tkinter.Tk()
    window.wm_withdraw()
    tkMessageBox.showerror(title="Uhh PERMISSION ERROR?!",message="There was a Permission Error..\nyou probably dont have any trophys on your vita!\nIt could be for another reason though..")
    os._exit(0)
except ftplib.socket.gaierror:
    import Tkinter
    window = Tkinter.Tk()
    window.wm_withdraw()
    tkMessageBox.showerror(title="Uhh CONNECTION ERROR!",message="There was a Connection Error..\nyou probably entered the IP wrong.")
    os._exit(0)
except:
    import Tkinter
    window = Tkinter.Tk()
    window.wm_withdraw()
    type, value, traceback = sys.exc_info()
    tkMessageBox.showerror(title="Uhh ERROR",message="There was an error.. type: "+str(type)+" value: "+str(value)+" traceback "+str(traceback))


