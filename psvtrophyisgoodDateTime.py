from Tkinter import *

import os

import ParseTRPTRNS
import VitaTime
try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import psvtrophyisgoodDateTime_support

def vp_start_gui(v0,v1):
    global timestamp
    global trophyid
    global npcommid
    trophyid = v1
    npcommid = v0
    ParseTRPTRNS.init(os.getcwd()+"/data/"+npcommid+"/TRPTRANS.DAT")
    timestamp = ParseTRPTRNS.parseTrophyDataBlock(trophyid)["timestamp"][0]
    timestamp = VitaTime.decodeTimestamp(timestamp)
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root.protocol("WM_DELETE_WINDOW", lambda: os._exit(0))
    root.resizable(0, 0)
    psvtrophyisgoodDateTime_support.set_Tk_var()
    top = Change_Timestamp (root)
    psvtrophyisgoodDateTime_support.init(root, top)
    root.mainloop()

w = None
def create_Change_Timestamp(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    psvtrophyisgoodDateTime_support.set_Tk_var()
    top = Change_Timestamp (w)
    psvtrophyisgoodDateTime_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Change_Timestamp():
    global w
    w.destroy()
    w = None


class Change_Timestamp:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("432x112+468+277")
        top.title("Change Timestamp")



        self.Label1 = Label(top)
        self.Label1.place(relx=0.02, rely=0.09, height=18, width=119)
        self.Label1.configure(text='''Select Date & Time''')

        self.yearBox = ttk.Combobox(top)
        self.yearBox.place(relx=0.05, rely=0.36, relheight=0.16
                , relwidth=0.16)
        self.value_list = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031,2032,2033,2034,2035,2036,2037,2038,2039,2040,2041,2042,2043,2044,2045,2046,2047,2048,2049,2050,2051,2052,2053,2054,2055,2056,2057,2058,2059,2060,2061,2062,2063,2064,2065,2066,2067,2068,2069,2070,2071,2072,2073,2074,2075,2076,2077,2078,2079,2080,2081,2082,2083,2084,2085,2086,2087,2088,2089,2090,2091,2092,2093,2094,2095,2096,2097,2098,2099]
        self.yearBox.configure(values=self.value_list)
        self.yearBox.configure(textvariable=psvtrophyisgoodDateTime_support.year)
        self.yearBox.configure(width=67)
        self.yearBox.configure(takefocus="")
        self.yearBox.set(timestamp.year)
        self.yearBox.bind("<Key>", lambda e: "break")

        self.monthBox = ttk.Combobox(top)
        self.monthBox.place(relx=0.23, rely=0.36, relheight=0.16, relwidth=0.2)
        self.value_list = ["January","Febuary","March","April","May","June","July","August","September","October","November","December"]
        self.monthBox.configure(values=self.value_list)
        self.monthBox.configure(textvariable=psvtrophyisgoodDateTime_support.mounth)
        self.monthBox.configure(width=87)
        self.monthBox.configure(takefocus="")
        self.monthBox.set(self.value_list[timestamp.month-1])
        self.monthBox.bind("<Key>", lambda e: "break")

        self.dayBox = ttk.Combobox(top)
        self.dayBox.place(relx=0.46, rely=0.36, relheight=0.16
                , relwidth=0.11)
        self.value_list = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
        self.dayBox.configure(values=self.value_list)
        self.dayBox.configure(textvariable=psvtrophyisgoodDateTime_support.day)
        self.dayBox.configure(width=47)
        self.dayBox.configure(takefocus="")
        self.dayBox.set(self.value_list[timestamp.month - 1])
        self.dayBox.bind("<Key>", lambda e: "break")

        self.hourBox = ttk.Combobox(top)
        self.hourBox.place(relx=0.63, rely=0.36, relheight=0.16
                , relwidth=0.09)
        self.value_list = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]
        self.hourBox.configure(values=self.value_list)
        self.hourBox.configure(textvariable=psvtrophyisgoodDateTime_support.hour)
        self.hourBox.configure(width=37)
        self.hourBox.configure(takefocus="")
        self.hourBox.set(self.value_list[timestamp.hour - 1])
        self.hourBox.bind("<Key>", lambda e: "break")

        self.minuteBox = ttk.Combobox(top)
        self.minuteBox.place(relx=0.74, rely=0.36, relheight=0.16
                , relwidth=0.09)
        self.value_list = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59"]
        self.minuteBox.configure(values=self.value_list)
        self.minuteBox.configure(textvariable=psvtrophyisgoodDateTime_support.minute)
        self.minuteBox.configure(width=37)
        self.minuteBox.configure(takefocus="")
        self.minuteBox.set(self.value_list[timestamp.minute - 1])
        self.minuteBox.bind("<Key>", lambda e: "break")

        self.secondBox = ttk.Combobox(top)
        self.secondBox.place(relx=0.86, rely=0.36, relheight=0.16
                , relwidth=0.09)
        self.value_list = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59"]
        self.secondBox.configure(values=self.value_list)
        self.secondBox.configure(textvariable=psvtrophyisgoodDateTime_support.second)
        self.secondBox.configure(width=37)
        self.secondBox.configure(takefocus="")
        self.secondBox.set(self.value_list[timestamp.second - 1])
        self.secondBox.bind("<Key>", lambda e: "break")

        self.Label2 = Label(top)
        self.Label2.place(relx=0.21, rely=0.36, height=18, width=8)
        self.Label2.configure(text='''-''')

        self.Label3 = Label(top)
        self.Label3.place(relx=0.44, rely=0.36, height=18, width=8)
        self.Label3.configure(text='''-''')

        self.Label4 = Label(top)
        self.Label4.place(relx=0.72, rely=0.36, height=18, width=8)
        self.Label4.configure(text=''':''')

        self.Label5 = Label(top)
        self.Label5.place(relx=0.83, rely=0.36, height=18, width=8)
        self.Label5.configure(text=''':''')

        self.applyButton = Button(top)
        self.applyButton.place(relx=0.05, rely=0.63, height=26, width=390)
        self.applyButton.configure(activebackground="#d9d9d9")
        self.applyButton.configure(command=lambda: psvtrophyisgoodDateTime_support.apply(trophyid,npcommid,self.yearBox.get(),self.monthBox.get(),self.dayBox.get(),self.hourBox.get(),self.minuteBox.get(),self.secondBox.get()))
        self.applyButton.configure(text='''Apply''')
        self.applyButton.configure(width=390)






if __name__ == '__main__':
    vp_start_gui()



