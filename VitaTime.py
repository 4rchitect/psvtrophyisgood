import datetime
import random


def decodeTimestamp(timestamp):
    timestamp = int(timestamp,16)
    dt = datetime.datetime.fromordinal(1) + datetime.timedelta(microseconds=timestamp)
    dt = dt.replace(microsecond=0)
    return dt
def encodeTimestamp(dateandtime):
    dt = datetime.datetime.strptime(dateandtime, "%Y-%m-%d %H:%M:%S.%f")
    timestamp = (dt - datetime.datetime(1, 1, 1)).total_seconds() * 1000000
    timestamp = hex(int(timestamp))[2:]
    if timestamp.endswith("L"):
        timestamp = timestamp[:-1]
    return timestamp


def genRandomTime():
    max = int(encodeTimestamp(str(datetime.datetime.now())),16)
    min = 63082281600000000
    timestamp = random.randrange(min,max)
    timestamp = hex(int(timestamp))[2:]
    if timestamp.endswith("L"):
        timestamp = timestamp[:-1]
    return timestamp