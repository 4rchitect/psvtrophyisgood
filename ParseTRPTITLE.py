import binascii


def init(v):
    global path
    path = v
    global trpTitle
    trpTitle = open(path,"rb").read()

def findDataZone(v):
    begin = 0x19c7
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
    timestamp = [dataBlock[51:51+15],dataBlock[68:68+15]]

    if unlocked == "01":
        unlocked = True
    else:
        unlocked = False
    return {"unlocked":unlocked,"timestamp":timestamp}

def zeroOutDataBlock(v):
    dataBlock = getDataBlock(v)
    newDataBlock = "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    dataBlock = binascii.unhexlify(dataBlock)
    newDataBlock = binascii.unhexlify(newDataBlock)
    trpTitle = open(path,"rb").read()
    trpTitle = trpTitle.replace(dataBlock,newDataBlock)
    open(path,"wb").write(trpTitle)



init("/home/silicaandpina/psvita/GIT/psvtrophyisgood/trophyDownloaded/data/NPWR09521_00_decrypted/TRPTITLE.DAT")
print getDataBlock(2)
print parseDataBlock(1)