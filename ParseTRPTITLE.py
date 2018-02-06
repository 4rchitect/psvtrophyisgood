import binascii
import ParseTRPSFM
import re


def init(v):
    global path
    path = v
    global trpTitle
    trpTitle = open(path,"rb").read()

def getNpCommId():
    try:
        a = trpTitle.index("NPWR")
    except:
        try:
            a = trpTitle.index("NPXS") ##Nptrophy Sample Code.. dont think anyhing else uses this
        except:
            ""
    npCommId = trpTitle[a:]
    npCommId = npCommId[:0x0c]
    return npCommId



def findDataZone(v):
    ParseTRPSFM.init("conf/"+getNpCommId()+"/TROP.SFM")
    b = ParseTRPSFM.getNumberOfTrophies()
    v = b - v
    begin = re.compile("\x50..........................................................................................\x08").search(trpTitle).start()
    end = begin + 0x5c
    a = 0
    while a != v:
        begin += 0x5c + 0x04
        end = begin + 0x5c
        a += 1
    return {"begin": begin, "end": end}

def getDataBlock(v):
     return binascii.hexlify(trpTitle[findDataZone(v)["begin"]:findDataZone(v)["end"]])

def parseDataBlock(v):
    dataBlock = getDataBlock(v)
    unlocked = dataBlock[32:34]
    timestamp = dataBlock[51:51+15]

    if unlocked == "01":
        unlocked = True
    else:
        unlocked = False
    return {"unlocked":unlocked,"timestamp":timestamp}

def unSyncTrophy(v):
    dataBlock = getDataBlock(v)
    idInHex = hex(v)[2:]
    if len(idInHex) != 2:
        idInHex = "0" + idInHex
    newDataBlock = "500000000000000000000000"+idInHex+"00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000008"
    dataBlock = binascii.unhexlify(dataBlock)
    newDataBlock = binascii.unhexlify(newDataBlock)
    trpTitle = open(path,"rb").read()
    trpTitle = trpTitle.replace(dataBlock,newDataBlock)
    open(path,"wb").write(trpTitle)


