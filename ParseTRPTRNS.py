import binascii

import os

import ParseTRPSFM
import ParseTRPTITLE
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
    return int(str(binascii.hexlify(trpData[0x187:0x188])),16)

def setNumberOfUnlockedTrophies(unlockedTrophys):
    if unlockedTrophys > 0xFF & unlockedTrophys < 0x00:
        return "Too Long!"
    numToWrite = hex(unlockedTrophys)[2:]
    if numToWrite.endswith("L"):
        numToWrite = numToWrite[:-1]
    if len(numToWrite) == 1:
        numToWrite = "0" + numToWrite
    trpData = binascii.hexlify(open(readPath, "rb").read())
    a = trpData[:782]
    b = trpData[784:]
    trpData = a+numToWrite+b
    open(readPath, "wb").write(binascii.unhexlify(trpData))


def getNpCommId():
    return trpData[0x170:0x170 + 0x0C]

def getNpCommSign():
    return binascii.hexlify(trpData[400:560])

def findDataZone(v):
        begin = 0x367
        end = begin + 0xAC
        a = 0
        while a != v:
            begin += 0xb0
            end = begin + 0xAC
            a += 1
        return {"begin":begin,"end":end}

def getTrophyDataBlock(v):
    begin = findDataZone(v)["begin"]
    end = findDataZone(v)["end"]
    return binascii.hexlify(trpData[begin:end])

def findDataBlockForTrophy(trophyId):
    a = 0
    ParseTRPSFM.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/conf/"+getNpCommId()+"/TROP.SFM")
    numTrophys = ParseTRPSFM.getNumberOfTrophies()
    while a != numTrophys:
        if parseTrophyDataBlock(a)["trophyId"] == trophyId:
            return a
        a += 1
    return -1


def writeTimestamp(v,timestamp):
    dataBlock = getTrophyDataBlock(v)
    a = dataBlock[:116]
    b = dataBlock[146:]
    newDataBlock = a + timestamp + "00" + timestamp + b
    dataBlock = binascii.unhexlify(dataBlock)
    newDataBlock = binascii.unhexlify(newDataBlock)
    trpData = open(readPath, "rb").read()
    trpData = trpData.replace(dataBlock, newDataBlock)
    open(readPath, "wb").write(trpData)

def findFreeTrophyDataBlock():
    a = 1
    while a != 0xFF:
        if parseTrophyDataBlock(a)["unlocked"] == False:
            break
        a += 1
    return a

def setAccountId(aid):
    a = trpData[:0x120]
    b = trpData[0x120+0x8:]
    newTrpData = a + binascii.unhexlify(aid) + b
    if aid == "0000000000000000":
        a = newTrpData[:0x18b]
        b = newTrpData[0x18c:]
        newTrpData = a + "\x00" + b
    else:
        a = newTrpData[:0x18b]
        b = newTrpData[0x18c:]
        newTrpData = a + "\x01" + b
    open(readPath, "wb").write(newTrpData)


def unlockTrophy(v):
    isUnlocked = findDataBlockForTrophy(v)
    if isUnlocked == -1:
        dataBlockId = findFreeTrophyDataBlock()
    else:
        dataBlockId = findDataBlockForTrophy(v)
    origTrophyDataBlock = getTrophyDataBlock(dataBlockId)
    npCommId = getNpCommId()

    ParseTRPSFM.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/conf/"+npCommId+"/TROP.SFM")
    grade = ParseTRPSFM.getAllTrophies()[v]["grade"]
    if grade == "P":
        grade = "01"
    elif grade == "G":
        grade = "02"
    elif grade == "S":
        grade = "03"
    elif grade == "B":
        grade = "04"

    trophyIdHEX = hex(v)[2:]
    if trophyIdHEX.endswith("L"):
        trophyIdHEX = trophyIdHEX[:-1]
    if len(trophyIdHEX) == 1:
        trophyIdHEX = "0" + trophyIdHEX


    a = origTrophyDataBlock[96+2:]
    b = origTrophyDataBlock[:96]
    trophyDataBlock = b + grade + a
    a = trophyDataBlock[32+2:]
    b = trophyDataBlock[:32]
    trophyDataBlock = b + "02" + a
    a = trophyDataBlock[102+2:]
    b = trophyDataBlock[:102]
    trophyDataBlock = b + "20" + a
    a = trophyDataBlock[88+2:]
    b = trophyDataBlock[:88]
    trophyDataBlock = b + trophyIdHEX + a

    trpData = open(readPath, "rb").read()
    trpData = trpData.replace(binascii.unhexlify(origTrophyDataBlock),binascii.unhexlify(trophyDataBlock))
    open(readPath,"wb").write(trpData)
    init(readPath)
    if isUnlocked != -1:
        writeTimestamp(dataBlockId, "00000000000000")
        init(readPath)
        unlockedTrophys = getNumberOfUnlockedTrophies() + 1
        setNumberOfUnlockedTrophies(unlockedTrophys)
    ParseTRPTITLE.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/data/"+getNpCommId()+"/TRPTITLE.DAT")
    ParseTRPTITLE.unlockTrophy(v)



def lockTrophy(v):
    dataBlockId = findDataBlockForTrophy(v)
    origTrophyDataBlock = getTrophyDataBlock(dataBlockId)
    a = origTrophyDataBlock[96+2:]
    b = origTrophyDataBlock[:96]
    trophyDataBlock = b + "00" + a
    a = trophyDataBlock[32+2:]
    b = trophyDataBlock[:32]
    trophyDataBlock = b + "00" + a
    a = trophyDataBlock[102+2:]
    b = trophyDataBlock[:102]
    trophyDataBlock = b + "00" + a
    a = trophyDataBlock[88+2:]
    b = trophyDataBlock[:88]
    trophyDataBlock = b + "00" + a

    trpData = open(readPath, "rb").read()
    trpData = trpData.replace(binascii.unhexlify(origTrophyDataBlock),binascii.unhexlify(trophyDataBlock))
    open(readPath,"wb").write(trpData)
    init(readPath)
    writeTimestamp(dataBlockId,"00000000000000")
    if dataBlockId == -1:
        unlockedTrophys = getNumberOfUnlockedTrophies() - 1
        setNumberOfUnlockedTrophies(unlockedTrophys)
    ParseTRPTITLE.init(os.path.dirname(os.path.realpath(__file__))+"/trophyDownloaded/data/" + getNpCommId() + "/TRPTITLE.DAT")
    ParseTRPTITLE.lockTrophy(v)


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
    trophyId = int(trophyDataBlock[88:88+2],16)
    return {"grade":trophyType,"unlocked":unlocked,"timestamp":timestamp,"trophyId":trophyId}

