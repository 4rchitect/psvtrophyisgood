import binascii

def init(path):
    global trpData
    global readPath
    readPath = path
    trpData = open(path, "rb").read()

def getAccountId():
    return binascii.hexlify(trpData[0x120:0x120+0x8])

def makeCmaAid(aid):
    cmaAid = [aid[i:i + 2] for i in range(0, len(aid), 2)]
    cmaAid.reverse()
    return str(cmaAid)
def getNumberOfUnlockedTrophies():
    return int(str(binascii.hexlify(trpData[0x187:0x187+0x1])),16)

def getNpCommId():
    return trpData[0x170:0x170 + 0x0C]

def getNpCommSign():
    return binascii.hexlify(trpData[0x190:0x190 + 0xAC])

def findDataZone(v):
        begin = 0x2B7
        end = begin + 0xAC
        a = 0
        while a != v:
            begin += 0xAC +0x04
            end = begin + 0xAC
            a += 1
        return {"begin":begin,"end":end}

def getTrophyDataBlock(v):
    begin = findDataZone(v)["begin"]
    end = findDataZone(v)["end"]
    return binascii.hexlify(trpData[begin:end])

def writeTimestamp(v,timestamp):
    origTrophyDataBlock = binascii.unhexlify(getTrophyDataBlock(v))
    ts = parseTrophyDataBlock(v)["timestamp"]
    trophyDataBlock = origTrophyDataBlock.replace(binascii.unhexlify(ts[0]),binascii.unhexlify(timestamp))
    trophyDataBlock = trophyDataBlock.replace(binascii.unhexlify(ts[1]),binascii.unhexlify(timestamp))
    trpData = open(readPath, "rb").read()
    trpData = trpData.replace(origTrophyDataBlock,trophyDataBlock)
    open(readPath,"wb").write(trpData)





def parseTrophyDataBlock(v):
    trophyDataBlock = getTrophyDataBlock(v)
    trophyType = trophyDataBlock[96:96 + 2]
    if trophyType == "01":
        trophyType = "P"
    elif trophyType == "02":
        trophyType = "G"
    elif trophyType == "03":
        trophyType = "S"
    elif trophyType == "04":
        trophyType = "B"
    else:
        trophyType = "Unknown"
    unlocked = trophyDataBlock[32:32+2]
    if unlocked == "02":
        unlocked = True
    elif unlocked == "00":
        unlocked = False
    else:
        unlocked = "Unknown"
    timestamp = [0,0]
    timestamp[0] = trophyDataBlock[116:116+14]
    timestamp[1] = trophyDataBlock[132:132+14]

    return {"grade":trophyType,"unlocked":unlocked,"timestamp":timestamp}

