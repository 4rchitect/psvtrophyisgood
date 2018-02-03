import datetime


def decodeTimestamp(timestamp):
    timestamp = int(timestamp,16)
    return datetime.datetime.fromordinal(1) + datetime.timedelta(microseconds=timestamp)

def encodeTimestamp(dateandtime):
    dt = datetime.datetime.strptime(dateandtime, "%Y-%m-%d %H:%M:%S.%f")
    timestamp = (dt - datetime.datetime(1, 1, 1)).total_seconds() * 1000000
    timestamp = hex(int(timestamp))[2:]
    if timestamp.endswith("L"):
        timestamp = timestamp[:-1]
    return timestamp