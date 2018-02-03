


def init(path):
    global sfmData
    sfmData = open(path,"rb").read()

def getSetInfo():
    a = sfmData.index("<title-name>")+len("<title-name>")
    setName = sfmData[a:]
    b = setName.index("</title-name>")
    setName = setName[:b]
    a = sfmData.index("<title-detail>")+len("<title-detail>")
    setDesc = sfmData[a:]
    b = setDesc.index("</title-detail>")
    setDesc = setDesc[:b]
    return {"title":setName,"desc":setDesc}


def getSfmSignature():
    a = sfmData.index("<!--Sce-Np-Trophy-Signature: ")+len("<!--Sce-Np-Trophy-Signature: ")
    b = sfmData[a:].index("-->")
    return sfmData[a:b]

def getTrophyData(v):
    v = str(v)
    while len(v) != 3:
        v = "0" + v
    a = sfmData.index('<trophy id="{}"'.format(v))
    trpData = sfmData[a:]
    b = trpData.index('</trophy>'.format(v))+len("</trophy>")
    trpData = trpData[:b]
    return trpData

def parseTrophyData(v):
    trpData = getTrophyData(v)
    a = trpData.index('hidden="')+len('hidden="')
    isHidden = trpData[a:]
    b = isHidden.index('"')
    isHidden = isHidden[:b]

    if isHidden == "no":
        isHidden = False
    else:
        isHidden = True

    a = trpData.index('ttype="')+len('ttype="')
    grade = trpData[a:]
    b = grade.index('"')
    grade = grade[:b]

    a = trpData.index('<name>')+len('<name>')
    name = trpData[a:]
    b = name.index('</name>')
    name = name[:b]

    a = trpData.index('<detail>')+len('<detail>')
    desc = trpData[a:]
    b = desc.index('</detail>')
    desc = desc[:b]

    return {"hidden":isHidden,"grade":grade,"name":name,"desc":desc}


def getAllTrophies():
    a = 0
    numTrophys = getNumberOfTrophies()
    trophys = []
    while a != numTrophys:
        trophys.append(parseTrophyData(a))
        a += 1

    trophys.append("")
    trophys.reverse()
    return trophys

def getNumberOfTrophies():
    a = 0
    while True:
        try:
            getTrophyData(a)
            a += 1
        except:
            break
    return a
