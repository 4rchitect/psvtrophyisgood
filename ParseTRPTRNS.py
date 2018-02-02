import datetime
import binascii

trpFile = "C:\Users\Matthew\Documents\PSVTROPHYISGOOD\data\DecryptedData\TRPTRANS.DAT"

trpData = open(trpFile, "rb").read()


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

def decodeTimestamp(timestamp):
    timestamp = int(timestamp,16)
    return datetime.datetime.fromordinal(1) + datetime.timedelta(microseconds=timestamp)

def encodeTimestamp(dateandtime):
    dt = datetime.datetime.strptime(dateandtime, "%Y-%m-%d %H:%M:%S.%f")
    timestamp = (dt - datetime.datetime(1, 1, 1)).total_seconds() * 1000000
    return hex(int(timestamp))[2:-1]
