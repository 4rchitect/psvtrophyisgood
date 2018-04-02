
from Tkinter import *

import datetime

import VitaTime

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import psvtrophyisgoodRandomTime_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    psvtrophyisgoodRandomTime_support.set_Tk_var()
    top = Randomize_Timestamp (root)
    psvtrophyisgoodRandomTime_support.init(root, top)
    root.mainloop()

w = None
def create_Randomize_Timestamp(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    psvtrophyisgoodRandomTime_support.set_Tk_var()
    top = Randomize_Timestamp (w)
    psvtrophyisgoodRandomTime_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Randomize_Timestamp():
    global w
    w.destroy()
    w = None


class Randomize_Timestamp:
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

        top.geometry("432x188+468+277")
        top.title("Randomize Timestamp")
        top.configure(highlightcolor="black")

        global timestamp
        timestamp = datetime.datetime.now()
        global timestamp2
        timestamp2 = VitaTime.decodeTimestamp("E01D003A63A000")


        self.ranStart = Label(top)
        self.ranStart.place(relx=0.02, rely=0.05, height=19, width=88)
        self.ranStart.configure(activebackground="#f9f9f9")
        self.ranStart.configure(cursor="fleur")
        self.ranStart.configure(text='''Random Start''')

        self.Year = ttk.Combobox(top)
        self.Year.place(relx=0.05, rely=0.21, relheight=0.1, relwidth=0.16)
        self.value_list = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031,2032,2033,2034,2035,2036,2037,2038,2039,2040,2041,2042,2043,2044,2045,2046,2047,2048,2049,2050,2051,2052,2053,2054,2055,2056,2057,2058,2059,2060,2061,2062,2063,2064,2065,2066,2067,2068,2069,2070,2071,2072,2073,2074,2075,2076,2077,2078,2079,2080,2081,2082,2083,2084,2085,2086,2087,2088,2089,2090,2091,2092,2093,2094,2095,2096,2097,2098,2099,]
        self.Year.configure(values=self.value_list)
        self.Year.configure(textvariable=psvtrophyisgoodRandomTime_support.year)
        self.Year.configure(takefocus="")
        self.Year.set(timestamp2.year)
        self.Year.bind("<Key>", lambda e: "break")

        self.Mounth = ttk.Combobox(top)
        self.Mounth.place(relx=0.23, rely=0.21, relheight=0.1, relwidth=0.2)
        self.value_list = ["January","Febuary","March","April","May","June","July","August","September","October","November","December",]
        self.Mounth.configure(values=self.value_list)
        self.Mounth.configure(textvariable=psvtrophyisgoodRandomTime_support.mounth)
        self.Mounth.configure(takefocus="")
        self.Mounth.configure(cursor="fleur")
        self.Mounth.set(self.value_list[timestamp2.month-1])
        self.Mounth.bind("<Key>", lambda e: "break")

        self.Day = ttk.Combobox(top)
        self.Day.place(relx=0.46, rely=0.21, relheight=0.1, relwidth=0.11)
        self.value_list = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31",]
        self.Day.configure(values=self.value_list)
        self.Day.configure(textvariable=psvtrophyisgoodRandomTime_support.day)
        self.Day.configure(takefocus="")
        self.Day.set(self.value_list[timestamp2.day-1])
        self.Day.bind("<Key>", lambda e: "break")

        self.Minutes = ttk.Combobox(top)
        self.Minutes.place(relx=0.63, rely=0.21, relheight=0.1, relwidth=0.09)
        self.value_list = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24",]
        self.Minutes.configure(values=self.value_list)
        self.Minutes.configure(textvariable=psvtrophyisgoodRandomTime_support.minute)
        self.Minutes.configure(takefocus="")
        self.Minutes.set(timestamp2.minute)
        self.Minutes.bind("<Key>", lambda e: "break")

        self.Hours = ttk.Combobox(top)
        self.Hours.place(relx=0.74, rely=0.21, relheight=0.1, relwidth=0.09)
        self.value_list = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59",]
        self.Hours.configure(values=self.value_list)
        self.Hours.configure(textvariable=psvtrophyisgoodRandomTime_support.hour)
        self.Hours.configure(takefocus="")
        self.Hours.set(self.value_list[timestamp2.hour-1])
        self.Hours.bind("<Key>", lambda e: "break")

        self.secs = ttk.Combobox(top)
        self.secs.place(relx=0.86, rely=0.21, relheight=0.1, relwidth=0.09)
        self.value_list = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59",]
        self.secs.configure(values=self.value_list)
        self.secs.configure(textvariable=psvtrophyisgoodRandomTime_support.second)
        self.secs.configure(takefocus="")
        self.secs.set(self.value_list[timestamp2.second-1])
        self.secs.bind("<Key>", lambda e: "break")

        self.Label2 = Label(top)
        self.Label2.place(relx=0.21, rely=0.21, height=19, width=8)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(text='''-''')

        self.Label3 = Label(top)
        self.Label3.place(relx=0.44, rely=0.21, height=19, width=8)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(text='''-''')

        self.Label4 = Label(top)
        self.Label4.place(relx=0.72, rely=0.21, height=19, width=8)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(text=''':''')

        self.Label5 = Label(top)
        self.Label5.place(relx=0.83, rely=0.21, height=19, width=8)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(text=''':''')

        self.randomizeButton = Button(top)
        self.randomizeButton.place(relx=0.05, rely=0.8, height=26, width=390)
        self.randomizeButton.configure(activebackground="#d9d9d9")
        self.randomizeButton.configure(command=lambda: psvtrophyisgoodRandomTime_support.applyDates(self.Year.get(),self.Mounth.get(),self.Day.get(),self.Hours.get(),self.Minutes.get(),self.secs.get(),self.Year1.get(),self.Mounth1.get(),self.Day1.get(),self.Hours1.get(),self.Minutes1.get(),self.secs1.get()))
        self.randomizeButton.configure(text='''Randomize''')

        self.ranEnd = Label(top)
        self.ranEnd.place(relx=0.02, rely=0.37, height=19, width=86)
        self.ranEnd.configure(text='''Random End''')
        self.ranEnd.configure(width=86)

        self.Year1 = ttk.Combobox(top)
        self.Year1.place(relx=0.05, rely=0.53, relheight=0.1, relwidth=0.16)
        self.value_list = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031,2032,2033,2034,2035,2036,2037,2038,2039,2040,2041,2042,2043,2044,2045,2046,2047,2048,2049,2050,2051,2052,2053,2054,2055,2056,2057,2058,2059,2060,2061,2062,2063,2064,2065,2066,2067,2068,2069,2070,2071,2072,2073,2074,2075,2076,2077,2078,2079,2080,2081,2082,2083,2084,2085,2086,2087,2088,2089,2090,2091,2092,2093,2094,2095,2096,2097,2098,2099,]
        self.Year1.configure(values=self.value_list)
        self.Year1.configure(textvariable=psvtrophyisgoodRandomTime_support.year2)
        self.Year1.configure(takefocus="")
        self.Year1.set(timestamp.year)
        self.Year1.bind("<Key>", lambda e: "break")

        self.Mounth1 = ttk.Combobox(top)
        self.Mounth1.place(relx=0.23, rely=0.53, relheight=0.1, relwidth=0.2)
        self.value_list = ["January","Febuary","March","April","May","June","July","August","September","October","November","December",]
        self.Mounth1.configure(values=self.value_list)
        self.Mounth1.configure(textvariable=psvtrophyisgoodRandomTime_support.mounth2)
        self.Mounth1.configure(takefocus="")
        self.Mounth1.set(self.value_list[timestamp.month-1])
        self.Mounth1.bind("<Key>", lambda e: "break")

        self.Day1 = ttk.Combobox(top)
        self.Day1.place(relx=0.46, rely=0.53, relheight=0.1, relwidth=0.11)
        self.value_list = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31",]
        self.Day1.configure(values=self.value_list)
        self.Day1.configure(textvariable=psvtrophyisgoodRandomTime_support.day2)
        self.Day1.configure(takefocus="")
        self.Day1.set(self.value_list[timestamp.day-1])
        self.Day1.bind("<Key>", lambda e: "break")


        self.Minutes1 = ttk.Combobox(top)
        self.Minutes1.place(relx=0.63, rely=0.53, relheight=0.1, relwidth=0.09)
        self.value_list = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24",]
        self.Minutes1.configure(values=self.value_list)
        self.Minutes1.configure(textvariable=psvtrophyisgoodRandomTime_support.hour2)
        self.Minutes1.configure(takefocus="")
        self.Minutes1.set(timestamp.minute)
        self.Minutes1.bind("<Key>", lambda e: "break")

        self.Hours1 = ttk.Combobox(top)
        self.Hours1.place(relx=0.74, rely=0.53, relheight=0.1, relwidth=0.09)
        self.value_list = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59",]
        self.Hours1.configure(values=self.value_list)
        self.Hours1.configure(textvariable=psvtrophyisgoodRandomTime_support.minute2)
        self.Hours1.configure(takefocus="")
        self.Hours1.set(self.value_list[timestamp.hour-1])
        self.Hours1.bind("<Key>", lambda e: "break")

        self.secs1 = ttk.Combobox(top)
        self.secs1.place(relx=0.86, rely=0.53, relheight=0.1, relwidth=0.09)
        self.value_list = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59",]
        self.secs1.configure(values=self.value_list)
        self.secs1.configure(textvariable=psvtrophyisgoodRandomTime_support.second2)
        self.secs1.configure(takefocus="")
        self.secs1.set(self.value_list[timestamp.second-1])
        self.secs1.bind("<Key>", lambda e: "break")

        self.Label7 = Label(top)
        self.Label7.place(relx=0.83, rely=0.53, height=19, width=8)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(text=''':''')
        self.Label7.configure(width=8)

        self.Label8 = Label(top)
        self.Label8.place(relx=0.72, rely=0.53, height=19, width=8)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(text=''':''')

        self.Label9 = Label(top)
        self.Label9.place(relx=0.44, rely=0.53, height=19, width=8)
        self.Label9.configure(activebackground="#f9f9f9")
        self.Label9.configure(text='''-''')

        self.Label10 = Label(top)
        self.Label10.place(relx=0.21, rely=0.53, height=19, width=8)
        self.Label10.configure(activebackground="#f9f9f9")
        self.Label10.configure(text='''-''')






if __name__ == '__main__':
    vp_start_gui()



