import binascii
import ParseTRPSFM
import re


def init(v):
    global path
    path = v
    global trpTitle
    trpTitle = open(path,"rb").read()

def getNpCommId():
    init(path)
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
    init(path)
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
    print {"begin": begin, "end": end}
    return {"begin": begin, "end": end}

def getDataBlock(v):
     return binascii.hexlify(trpTitle[findDataZone(v)["begin"]:findDataZone(v)["end"]])

def parseDataBlock(v):
    dataBlock = getDataBlock(v)
    unlocked = dataBlock[32:34]
    timestamp = dataBlock[52:66]
    timestamp2 = dataBlock[68:67+15]
    if unlocked == "01":
        unlocked = True
    else:
        unlocked = False
    return {"unlocked":unlocked,"timestamp":timestamp,"timestamp2":timestamp2}

def unlockTrophy(v):
    dataBlock = getDataBlock(v)
    a = dataBlock[32:]
    b = dataBlock[34:]
    newDataBlock = a + "01" + b
    dataBlock = binascii.unhexlify(dataBlock)
    newDataBlock = binascii.unhexlify(newDataBlock)
    trpTitle = open(path,"rb").read()
    trpTitle = trpTitle.replace(dataBlock,newDataBlock)
    open(path,"wb").write(trpTitle)

def lockTrophy(v):
    dataBlock = getDataBlock(v)
    a = dataBlock[32:]
    b = dataBlock[34:]
    newDataBlock = a + "00" + b
    dataBlock = binascii.unhexlify(dataBlock)
    newDataBlock = binascii.unhexlify(newDataBlock)
    trpTitle = open(path,"rb").read()
    trpTitle = trpTitle.replace(dataBlock,newDataBlock)
    open(path,"wb").write(trpTitle)
    init(path)
    writeTimestamp(v, "00000000000000")

def writeTimestamp(v,timestamp):
    init(path)
    origTrophyDataBlock = binascii.unhexlify(getDataBlock(v))
    ts = [parseDataBlock(v)["timestamp"],parseDataBlock(v)["timestamp2"]]
    trophyDataBlock = origTrophyDataBlock.replace(binascii.unhexlify(ts[0]),binascii.unhexlify(timestamp))
    trophyDataBlock = trophyDataBlock.replace(binascii.unhexlify(ts[1]),binascii.unhexlify(timestamp))
    trpTitle = open(path, "rb").read()
    trpTitle = trpTitle.replace(origTrophyDataBlock,trophyDataBlock)
    open(path,"wb").write(trpTitle)

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


