##Unused, the trophy_local.db is acturally terrible for getting trophy info.
##File still left in here incase anyone wants it though.

import sqlite3

def init(path):
    global sqlHandle
    sqlHandle = sqlite3.connect(path)



def getSetInfo(v):
    sqlCursor = sqlHandle.cursor()
    sqlCursor.execute("SELECT * FROM tbl_trophy_title")
    rows = sqlCursor.fetchall()
    return {"npCommId":rows[v][3],"numTrophies":rows[v][31],"title":rows[v][42]}

def geSetInfoByNpCommId(npCommId):
    a = 0
    while True:
        if getSetInfo(a)["npCommId"] == npCommId:
            return getSetInfo(a)
        a += 1


def getTrophysInSet(npCommId):
    sqlCursor = sqlHandle.cursor()
    sqlCursor.execute("SELECT * FROM tbl_trophy_flag")
    rows = sqlCursor.fetchall()
    filteredRows = []
    for row in rows:
        if row.__contains__(npCommId):
            filteredRows.append(row)
    rows = None
    a = 0
    trophys = []

    while a != len(filteredRows):
        grade = filteredRows[a][11]
        if grade == 1:
            grade = "P"
        elif grade == 2:
            grade = "G"
        elif grade == 3:
            grade = "S"
        elif grade == 4:
            grade = "B"
        else:
            grade = "Unknown"
        trophys.append({"grade":grade,"title":filteredRows[a][13],"description":filteredRows[a][14],"trophyId":filteredRows[a][4]})
        a += 1

    trophys.reverse()
    return trophys
