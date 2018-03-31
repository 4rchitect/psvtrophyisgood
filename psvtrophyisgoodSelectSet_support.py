import os
import shutil

import sys

import ParseTRPSFM
import psvtrophyisgoodModTRP
import tkFileDialog
import tkMessageBox


try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1


def selectSet(indexTitle):
    if len(indexTitle) == 0:
        tkMessageBox.showerror(title="Fail!", message="You have no trophys imported.")
    else:
        npCommId = indexTitle[indexTitle.index("[")+1:]
        npCommId = npCommId[:-1]
        #print "Decrypting "+npCommId
        #PFS.decryptPFS(os.getcwd()+"/data/"+npCommId)
        destroy_window()
        psvtrophyisgoodModTRP.vp_start_gui(npCommId)

def exportSet(indexTitle):
    npCommId = indexTitle[indexTitle.index("[")+1:]
    npCommId = npCommId[:-1]
    exportFolder = tkFileDialog.askdirectory(title="Export to:")
    try:
        shutil.copytree(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/data/" + npCommId, exportFolder + "/data/" + npCommId)
        shutil.copytree(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/conf/" + npCommId, exportFolder + "/conf/"+npCommId)
        tkMessageBox.showinfo(title="Done!", message="Exported trophy set " + npCommId + " to " + exportFolder)
    except:
        type, value, traceback = sys.exc_info()
        tkMessageBox.showerror(title="Fail!",message="Error: "+str(type)+"\n"+str(value)+"\n"+str(traceback))


def importSet():
    tkMessageBox.showinfo(title="Done!", message="Please select the conf folder,\nand then the decrypted data folder.")
    confPath = tkFileDialog.askdirectory(title="CONF FOLDER")
    if os.path.exists(confPath+"/TROP.SFM"):
        try:
            ParseTRPSFM.init(confPath+"/TROP.SFM")
            npCommId = ParseTRPSFM.getNpCommid()
            shutil.copytree(confPath,os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/conf/"+npCommId)
            dataPath = tkFileDialog.askdirectory(title="DATA FOLDER")
            if os.path.exists(dataPath + "/TRPTRANS.DAT"):
                if os.path.exists(dataPath + "/TRPTITLE.DAT"):
                    if open(dataPath + "/TRPTRANS.DAT","rb").read().startswith("\x3E\x31\x8F\xBA"):
                        if open(dataPath + "/TRPTITLE.DAT","rb").read().startswith("\x17\xE6\x9B\x72"):
                            shutil.copytree(dataPath, os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/data/" + npCommId)
                        else:
                            tkMessageBox.showerror(title="Fail!", message="Invalid TRPTITLE.\nPlease make sure you only import decrypted data/ folders.")
                    else:
                        tkMessageBox.showerror(title="Fail!", message="Invalid TRPTRANS.\nPlease make sure you only import decrypted data/ folders.")
                else:
                    tkMessageBox.showerror(title="Fail!",message="TRPTITLE.DAT not found.")
            else:
                tkMessageBox.showerror(title="Fail!", message="TRPTRANS.DAT not found.")

        except:
            type, value, traceback = sys.exc_info()
            tkMessageBox.showerror(title="Fail!",message="Error: "+str(type)+"\n"+str(value)+"\n"+str(traceback))

    destroy_window()
    import psvtrophyisgoodSelectSet
    psvtrophyisgoodSelectSet.vp_start_gui()






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


