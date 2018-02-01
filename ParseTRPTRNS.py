import os
import binascii

trpFile = "C:\Users\Matthew\Documents\PSVTROPHYISGOOD\data\decrypted\TRPTRANS.DAT"

trpHandle = open(trpFile, "rb")


def getAccountId():
    return binascii.hexlify(trpHandle.read()[0x120:0x120+0x8])

def makeCmaAid(aid):
    cmaAid = [aid[i:i + 2] for i in range(0, len(aid), 2)]
    cmaAid.reverse()
    return str(cmaAid)
def getNumberOfUnlockedTrophies():
    return int(binascii.hexlify(trpHandle.read()[0x187:0x187+0x1]),16)

def getNpCommId():
    return trpHandle.read()[0x170:0x170 + 0x0C]

def getNpCommSign():
    return binascii.hexlify(trpHandle.read()[0x19C:0x19C + 0x94])

def findTownOfBeginings(v):
        begin = 0x2B7
        end = begin + 0xAC
        a = 0
        while a != v:
            begin += 0x2B7 #+ 0x05
            end = begin + 0xAC
            a += 1
        return {"begin":begin,"end":end}

def getTrophyDataBlock(v):
    begin = findTownOfBeginings(v)["begin"]
    end = findTownOfBeginings(v)["end"]
    return binascii.hexlify(trpHandle.read()[begin:end])


print getTrophyDataBlock(0)