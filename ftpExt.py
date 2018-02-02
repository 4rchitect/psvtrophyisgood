import os
import ftplib

def sortList(listing):
    a = 0
    dirs = []
    files = []
    while a != len(listing):
        words = listing[a].split(None, 8)
        filename = words[-1].lstrip()
        if listing[a].startswith("d"):
            dirs.append(filename)
        else:
            files.append(filename)
        a += 1
    return {"files":files,"dirs":dirs}

def downloadRecursive(ftpHandle):
    listing = []
    ftpHandle.retrlines("LIST", listing.append)
    listing = sortList(listing)
    numDirs =  len(listing["dirs"])
    numFiles = len(listing["files"])
    a = 0
    while a != numDirs:
        print "Checking if "+listing["dirs"][a]+" exist?"
        if not os.path.exists(listing["dirs"][a]):
            print "Creating directory: "+ listing["dirs"][a]
            os.mkdir(listing["dirs"][a])
        a += 1
    a = 0
    while a != numFiles:
        print "Downloading: " + listing["files"][a]
        file = open(listing["files"][a], "wb")
        print ftpHandle.retrbinary("RETR " + listing["files"][a], file.write)
        file.close()
        a += 1
    a = 0
    while a != len(listing["dirs"]):
        if os.path.isdir(listing["dirs"][a]):
            ftpHandle.cwd(listing["dirs"][a])
            os.chdir(listing["dirs"][a])
        if len(listing["dirs"]) != 0:
            downloadRecursive(ftpHandle)
        a += 1
    ftpHandle.cwd("../")
    os.chdir("../")



