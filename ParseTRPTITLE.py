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

def setAccountId(aid):
    a = trpTitle[:0x1E0]
    b = trpTitle[0x1E0+0x8:]
    newtrpTitle = a + binascii.unhexlify(aid) + b
    open(path, "wb").write(newtrpTitle)

def findDataZone(v):
    global begin
    ParseTRPSFM.init("conf/"+getNpCommId()+"/TROP.SFM")
    b = ParseTRPSFM.getNumberOfTrophies()
    if v != 0:
        v = b - v
    else:
        v = b - 1
    trpTitle = open(path,"rb").read()
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
    timestamp = dataBlock[52:66]
    timestamp2 = dataBlock[68:82]
    if unlocked == "01":
        unlocked = True
    else:
        unlocked = False
    return {"unlocked":unlocked,"timestamp":timestamp,"timestamp2":timestamp2}

def unlockTrophy(v):
    dataBlock = getDataBlock(v)
    a = dataBlock[:32]
    b = dataBlock[34:]
    newDataBlock = a + "01" + b
    dataBlock = binascii.unhexlify(dataBlock)
    newDataBlock = binascii.unhexlify(newDataBlock)
    trpTitle = open(path,"rb").read()
    trpTitle = trpTitle.replace(dataBlock,newDataBlock)
    open(path,"wb").write(trpTitle)

def lockTrophy(v):
    dataBlock = getDataBlock(v)
    a = dataBlock[:32]
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
    dataBlock = getDataBlock(v)
    a = dataBlock[:52]
    b = dataBlock[82:]
    newDataBlock = a + timestamp + "00" + timestamp + b
    dataBlock = binascii.unhexlify(dataBlock)
    newDataBlock = binascii.unhexlify(newDataBlock)
    trpTitle = open(path, "rb").read()
    trpTitle = trpTitle.replace(dataBlock, newDataBlock)
    open(path, "wb").write(trpTitle)
