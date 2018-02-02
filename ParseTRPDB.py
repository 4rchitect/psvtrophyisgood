import sqlite3

def init(path):
    global sqlHandle
    sqlHandle = sqlite3.connect(path)

