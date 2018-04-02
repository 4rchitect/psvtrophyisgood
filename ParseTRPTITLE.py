import binascii
import re

def init(v):
    global trpTitle
    global path
    path = v
    trpTitle = open(path, 'rb').read()


def getNpCommId():
    try:
        a = trpTitle.index('NPWR')
    except:
        try:
            a = trpTitle.index('NPXS')
        except:
            pass

    npCommId = trpTitle[a:]
    npCommId = npCommId[:12]
    return npCommId


def setAccountId(aid):
    a = trpTitle[:480]
    b = trpTitle[488:]
    newtrpTitle = a + binascii.unhexlify(aid) + b
    open(path, 'wb').write(newtrpTitle)


def getProgress():
    trpTitle = open(path, 'rb').read()
    begin = findDataZone(0)['begin']
    begin -= 295
    end = begin + 16
    progress = trpTitle[begin:end]
    list = []
    list += progress
    list.reverse()
    progress = ''.join(list)
    progress = binascii.hexlify(progress)
    progress = int(progress, 16)
    return progress


def increaseProgress(trophy_id):
    progress = getProgress()
    progress |= (1 << trophy_id)
    return progress


def decreaseProgress(trophy_id):
    progress = getProgress()
    progress &= 0xFFFFFFFFFFFFFFFFFFFFFFFF ^ (1 << trophy_id)
    return progress


def setProgress(progress):
    progressHex = hex(progress)[2:]
    if progressHex.endswith('L'):
        progressHex = progressHex[:-1]
    while len(progressHex) != 32:
        progressHex = '0' + progressHex

    progressHex = binascii.unhexlify(progressHex)
    list = []
    list += progressHex
    list.reverse()
    progressHex = ''.join(list)
    trpTitle = open(path, 'rb').read()
    begin = findDataZone(0)['begin']
    begin -= 295
    end = begin + 16
    a = trpTitle[:begin]
    b = trpTitle[end:]
    trpTitle = a + progressHex + b
    open(path, 'wb').write(trpTitle)


def findDataZone(v):
    global begin
    trpTitle = open(path, 'rb').read()
    begin = re.compile('P..........................................................................................\x08').search(trpTitle).start()
    end = begin + 92
    a = 0
    while a != v:
        begin += 96
        end = begin + 92
        a += 1

    return {'begin': begin,
     'end': end}


def getDataBlock(v):
    return binascii.hexlify(trpTitle[findDataZone(v)['begin']:findDataZone(v)['end']])


def parseDataBlock(v):
    dataBlock = getDataBlock(v)
    unlocked = dataBlock[32:34]
    timestamp = dataBlock[52:66]
    timestamp2 = dataBlock[68:82]
    if unlocked == '01':
        unlocked = True
    else:
        unlocked = False
    return {'unlocked': unlocked,'timestamp': timestamp,'timestamp2': timestamp2}


def unlockTrophy(v):
    if not parseDataBlock(v)['unlocked']:
        setProgress(increaseProgress(v))
        init(path)
    dataBlock = getDataBlock(v)
    a = dataBlock[:32]
    b = dataBlock[34:]
    newDataBlock = a + '01' + b
    a = newDataBlock[:38]
    b = newDataBlock[40:]
    newDataBlock = a + '20' + b
    dataBlock = binascii.unhexlify(dataBlock)
    newDataBlock = binascii.unhexlify(newDataBlock)
    trpTitle = open(path, 'rb').read()
    trpTitle = trpTitle.replace(dataBlock, newDataBlock)
    open(path, 'wb').write(trpTitle)


def lockTrophy(v):
    dataBlock = getDataBlock(v)
    if parseDataBlock(v)['unlocked']:
        setProgress(decreaseProgress(v))
        init(path)
    a = dataBlock[:32]
    b = dataBlock[34:]
    newDataBlock = a + '00' + b
    a = newDataBlock[:38]
    b = newDataBlock[40:]
    newDataBlock = a + '00' + b
    dataBlock = binascii.unhexlify(dataBlock)
    newDataBlock = binascii.unhexlify(newDataBlock)
    trpTitle = open(path, 'rb').read()
    trpTitle = trpTitle.replace(dataBlock, newDataBlock)
    open(path, 'wb').write(trpTitle)
    init(path)
    writeTimestamp(v, '00000000000000')


def writeTimestamp(v, timestamp):
    dataBlock = getDataBlock(v)
    a = dataBlock[:52]
    b = dataBlock[82:]
    newDataBlock = a + timestamp + '00' + timestamp + b
    a = newDataBlock[:38]
    b = newDataBlock[40:]
    newDataBlock = a + '20' + b
    dataBlock = binascii.unhexlify(dataBlock)
    newDataBlock = binascii.unhexlify(newDataBlock)
    trpTitle = open(path, 'rb').read()
    trpTitle = trpTitle.replace(dataBlock, newDataBlock)
    open(path, 'wb').write(trpTitle)