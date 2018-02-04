
import Tkinter
import shutil
from ftplib import FTP
import tkSimpleDialog
import os
import ftpExt
import psvtrophyisgoodSelectSet





window = Tkinter.Tk()
window.wm_withdraw()
serverIp = tkSimpleDialog.askstring("FTP Connection","Please enter FTP Mode on your PSVITA, and enter the IP Below:")
window.destroy()

if serverIp == None:
    os.chdir("trophyDownloaded")
    psvtrophyisgoodSelectSet.vp_start_gui()
    os._exit(0)
if serverIp.endswith(":1337"):
    serverIp = serverIp[:-5]


if os.path.exists("trophyDownloaded/data"):
    shutil.rmtree("trophyDownloaded/data")
#if os.path.exists("trophyDownloaded/conf"):
#    shutil.rmtree("trophyDownloaded/conf")
#if os.path.exists("trophyDownloaded/db"): Fuck trophy_local.db
#    shutil.rmtree("trophyDownloaded/db")

if not os.path.exists("trophyDownloaded/db"):
    os.makedirs("trophyDownloaded/db")
if not os.path.exists("trophyDownloaded/data"):
    os.makedirs("trophyDownloaded/data")
if not os.path.exists("trophyDownloaded/conf"):
    os.makedirs("trophyDownloaded/conf")

print "Connecting to: "+serverIp
ftp = FTP()
print ftp.connect(serverIp,1337)
#print "Moving to ur0:/user/00/trophy/db"
#print ftp.cwd("/ur0:/user/00/trophy/db")
#print "Downloading trophy_local.db"

#dbFile = open("trophyDownloaded/db/trophy_local.db", "wb")
#print ftp.retrbinary("RETR trophy_local.db", dbFile.write)
#dbFile.close()

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
print ftp.cwd("/ur0:/user/00/trophy/data")
print "Downloading ur0:/user/00/trophy/data/*"
ftpExt.downloadRecursive(ftp)
ftp.close()

psvtrophyisgoodSelectSet.vp_start_gui()

os._exit(0)
