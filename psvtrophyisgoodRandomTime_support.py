import tkMessageBox
from Tkinter import *

import VitaTime

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

def set_Tk_var():
    global year
    year = StringVar()
    global mounth
    mounth = StringVar()
    global day
    day = StringVar()
    global hour
    hour = StringVar()
    global minute
    minute = StringVar()
    global second
    second = StringVar()

    global year2
    year2 = StringVar()
    global mounth2
    mounth2 = StringVar()
    global day2
    day2 = StringVar()
    global hour2
    hour2 = StringVar()
    global minute2
    minute2 = StringVar()
    global second2
    second2 = StringVar()

def applyDates(year, month, day, hour, minute, second,year2, month2, day2, hour2, minute2, second2):
    month = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October","November", "December"].index(month) + 1
    month2 = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October","November", "December"].index(month2) + 1
    try:
        global timestamp
        global timestamp2
        timestamp = VitaTime.encodeTimestamp("{}-{}-{} {}:{}:{}.{}".format(year, month, day, hour, minute, second, 0))
        timestamp2 = VitaTime.encodeTimestamp("{}-{}-{} {}:{}:{}.{}".format(year2, month2, day2, hour2, minute2, second2, 0))

        if int(timestamp2,16) <= int(timestamp,16):
            tkMessageBox.showerror(title="THAT MAKES NO SENSE!", message="End time is lower than start time.")
        else:
            destroy_window()

    except:
        tkMessageBox.showerror(title="THAT MAKES NO SENSE!", message="You entered an impossible time.")


def getTimestamps():
    timestamps = [timestamp,timestamp2]
    return timestamps

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import psvtrophyisgoodRandomTime
    psvtrophyisgoodRandomTime.vp_start_gui()


