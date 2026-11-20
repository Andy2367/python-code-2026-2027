import tkinter as tk
import sqlite3
import time
from win11toast import toast

def selected_cmd(filter, main, num_selected): # needs fixed, doesn't create any buttons.
    filter = "Selected"
    main.destroy()

    main = tk.Tk()

    main.geometry("600x650")  # sets the main window size
    selected_events = tk.Button(text="Selected Events", bg="grey", command= lambda: selected_cmd(filter, main, num_selected))  # creates the selected events btn which will automatically filter the results to show only the currently selected events.
    selected_events.place(relx= 0.05, rely= 0.05)

    filter_btn = tk.Button(text="     Filter     ", bg="grey")  # creates the filter btn which will (currently does not) create a new window with the filtering options.
    filter_btn.place(relx= 0.6, rely= 0.05)

    scrollwindow= tk.Canvas(main, bg="light grey")      # creates a canvas which will be used to allow scrolling
    scrollwindow.place(relwidth=0.9, relheight=0.75, relx = 0.05, rely=0.2)

    scrolbar = tk.Scrollbar(main, orient="vertical", command=scrollwindow.yview) # creates the scrollbar widget on the window
    scrolbar.place(relheight=0.75, relwidth=0.1, relx=0.9, rely= 0.2)

    scrollwindow.configure(yscrollcommand=scrolbar.set) # sets the position of the slider

    frame = tk.Frame(scrollwindow, bg="grey")      # creates a frame which is the same size as the scrollwindow canvas to allow the addition of widgets to it
    scrollwindow.create_window((0, 0), window=frame, anchor="nw")

    frame.bind(
        "<Configure>",
        lambda e: scrollwindow.configure(scrollregion=scrollwindow.bbox("all")) # sets the area that can be scrolled to the entire scroll window canvas
    )

    app = event(main, 1, 2, 3, 4, 5, 6, 7)
    for i in range(num_selected):
        app.create_btn(i+1, filter)


    main.mainloop()



class event:
    def __init__(self, main, name, event_type, location, event_time, event_date, more_info, selected):
        self.name = name
        self.event_type = event_type
        self.location = location
        self.event_time = event_time
        self.event_date = event_date
        self.more_info = more_info
        self.selected = selected
        self.main = main
        self.btns = {}

    def get_ststus(self, ID):
        conn = sqlite3.connect("IA_database.db")
        cur = conn.cursor()

        cur.execute("SELECT Selected FROM Events WHERE Event_id IS ?"(ID))
        status = cur.fetchone()
        status = int(status[0])
        return status


    def update_status(self, ID):
        conn = sqlite3.connect("IA_database.db")
        cur = conn.cursor()
        status = self.get_ststus(ID)
        if status == 0:
            print()
            print(self.get_ststus(ID))
            cur.execute(f"UPDATE Events SET Selected = 1 WHERE Event_id = {ID}")
            conn.commit()
            print(self.get_ststus(ID))
            print()
            self.btns[ID].config(bg="blue")
        elif status == 1:
            print()
            print(self.get_ststus(ID))
            cur.execute(f"UPDATE Events SET Selected = 0 WHERE Event_id = {ID}")
            conn.commit()
            print(self.get_ststus(ID))
            print()
            self.btns[ID].config(bg="light grey")

    def create_btn(self, ID, filter):

        if filter == "all":
            conn = sqlite3.connect("IA_database.db")
            cur = conn.cursor()
            cur.execute("SELECT Event_name FROM Events WHERE Event_id = ?"(ID)
            name = cur.fetchone()
            name = name[0]

            cur.execute("SELECT Event_type FROM Events WHERE Event_id = ?"(ID)
            e_type = cur.fetchone()
            e_type = e_type[0]

            cur.execute("SELECT Location FROM Events WHERE Event_id = ?"(ID)
            loc = cur.fetchone()
            loc = loc[0]

            cur.execute("SELECT Time FROM Events WHERE Event_id = ?"(ID))
            time = cur. fetchone()
            time = time[0]

            cur.execute("SELECT More_info FROM Events WHERE Event_id = ?"(ID)
            info = cur.fetchone()
            info = info[0]

            status = self.get_ststus(ID)

            cur.execute("SELECT  Date FROM Events WHERE Event_id = ? AND Selected = 1"(ID))
            date = cur.fetchone()           

            if status == 0:
                bg = "light grey"
            elif status == 1:
                bg = "blue"
            
            btn = tk.Button(frame, height=2, width=70,text=f"{name} {e_type}, in {loc}, at {time}, on {date}, get more info at {info}",bg=bg,command= lambda: self.update_status(ID))
            self.btns[ID] = btn
            btn.pack(padx=5, pady=5)


        elif filter == "selected":
            cur.execute("SELECT Event_name FROM Events WHERE Event_id = ? AND Selected = 1"(ID))
            name = cur.fetchone()
            name = name[0]

            cur.execute("SELECT Event_type FROM Events WHERE Event_id = ? AND Selected = 1"(ID))
            e_type = cur.fetchone()
            e_type = e_type[0]

            cur.execute("SELECT Location FROM Events WHERE Event_id = ? AND Selected = 1"(ID))
            loc = cur.fetchone()
            loc = loc[0]

            cur.execute("SELECT Time FROM Events WHERE Event_id = ? AND Selected = 1"(ID))
            time = cur. fetchone()
            time = time[0]

            cur.execute("SELECT More_info FROM Events WHERE Event_id = ? AND Selected = 1"(ID))
            info = cur.fetchone()
            info = info[0]

            status = self.get_ststus(ID)

            cur.execute("SELECT  Date FROM Events WHERE Event_id = ? AND Selected = 1"(ID))
            date = cur.fetchone()

            if status == 0:
                bg = "light grey"
            elif status == 1:
                bg = "blue"
            
            
            elif filter == "not_selected":
                conn = sqlite3.connect("IA_database.db")
                cur = conn.cursor()
                cur.execute("SELECT Event_name FROM Events WHERE Event_id = ? AND Selected = 0"(ID))
                name = cur.fetchone()
                name = name[0]

                cur.execute("SELECT Event_type FROM Events WHERE Event_id = ? AND Selected = 0"(ID))
                e_type = cur.fetchone()
                e_type = e_type[0]

                cur.execute("SELECT Location FROM Events WHERE Event_id = ? AND Selected = 0"(ID))
                loc = cur.fetchone()
                loc = loc[0]

                cur.execute("SELECT Time FROM Events WHERE Event_id = ? AND Selected = 0"(ID))
                time = cur. fetchone()
                time = time[0]

                cur.execute("SELECT More_info FROM Events WHERE Event_id = ? AND Selected = 0"(ID))
                info = cur.fetchone()
                info = info[0]

                status = self.get_ststus(ID)

                cur.execute("SELECT  Date FROM Events WHERE Event_id = ? AND Selected = 1"(ID))
                date = cur.fetchone()

                if status == 0:
                    bg = "light grey"
                elif status == 1:
                    bg = "blue"
                
                btn = tk.Button(frame,height=2, width=70, text=f"{name} {e_type}, in {loc}, at {time}, on {date}, get more info at {info}",bg=bg, command= lambda: self.update_status(ID))
                self.btns[ID] = btn
                btn.pack(padx=5, pady=5)

    def get_time(self, ID):
        cur.execute(f"SELECT Time FROM Events WHERE Event_id = {ID}")
        Time = cur.fetchone()
        Time = Time[0]
        return str(Time)

    def check_time(self, ID):
        AH = time.strftime("%h")
        AH = int(AH)
        AM = time.strftime("%m")
        AM = int(AM)
        ET  = self.get_time(ID)
        EH = ET[:1]
        EH = int(EH)
        EM = ET[-1]
        time_till_h = (EH - AH)
        Time = self.get_time(ID)
        cur.execute("SELECT Event_name FROM Events WHERE Event_id = ?"(ID))
        name = cur.fetchone()
        name = name[0]
        till_m = (EM - AM)
        if time_till_h < 0:
            print(f"{name} satrted as {Time}")
        elif time_till_h == 0:
            if till_m <= 0:
                toast(f"{name} is starting")
            elif till_m > 0:
                toast(f"{name} is starting in {till_m} minutes")
        elif time_till_h < 0:
            if till_m == 30:
                toast(f"{name} starts in 30 minutes")
            elif till_m == 10:
                toast(f"{name} starts in 10 minutes", on_click=self.more_info)

# connect to database or create one if it does not exist
conn = sqlite3.connect("IA_database.db")
cur = conn.cursor()

# create all required tables if they don't exist

c1 = """CREATE TABLE IF NOT EXISTS
Events(Event_id INTEGER PRIMARY KEY,
Event_name TEXT,
Event_type INTEGER,
Location INTEGER,
Time DATETIME,
More_info TEXT,
Selected INTEGER NOT NULL DEFAULT 0 CHECK(SELECTED IN (0,1)))""" # BOOL data type

c2 = """CREATE TABLE IF NOT EXISTS
Locations(location_id INTEGER PRIMARY KEY,
location_name TEXT)"""

c3 = """CREATE TABLE IF NOT EXISTS
Event_types(type_id INTEGER PRIMARY KEY,
type_name TEXT)"""

cur.execute(c1) # creates Events table
cur.execute(c2) # creates Locations table
cur.execute(c3) #creates Event type table

conn.commit() # saves changes to the db (should be added after every block of executes for redundancy)

cur.execute("SELECT COUNT (*) FROM Events")
num_events = cur.fetchone()
num_events = num_events[0]

cur.execute("SELECT COUNT (*) FROM Events WHERE Selected = 1")
num_selected = cur.fetchone()
num_selected = num_selected[0]
print(num_selected)

filter = "all"

main = tk.Tk()

main.geometry("600x650")  # sets the main window size
selected_events = tk.Button(text="Selected Events", bg="grey", command= lambda: selected_cmd(filter, main, num_selected))  # creates the selected events btn which will automaticly filter the results to show only the currently selected events.
selected_events.place(relx= 0.05, rely= 0.05)

filter_btn = tk.Button(text="     Filter     ", bg="grey")  # creates the filter btn which will (currently does not) creat a new window with the filtering options.
filter_btn.place(relx= 0.6, rely= 0.05)

scrollwindow= tk.Canvas(main, bg="light grey")      # creates a canvas which will be used to allow scrolling
scrollwindow.place(relwidth=0.9, relheight=0.75, relx = 0.05, rely=0.2)

scrolbar = tk.Scrollbar(main, orient="vertical", command=scrollwindow.yview) # creates the scrollbar widget on the window
scrolbar.place(relheight=0.75, relwidth=0.1, relx=0.9, rely= 0.2)

scrollwindow.configure(yscrollcommand=scrolbar.set) # sets the position of the slider

frame = tk.Frame(scrollwindow, bg="grey")      # creates a frame which is the same size as the scrollwindow canvas to allow the addition of widgets to it
scrollwindow.create_window((0, 0), window=frame, anchor="nw")

frame.bind(
    "<Configure>",
    lambda e: scrollwindow.configure(scrollregion=scrollwindow.bbox("all")) # sets the area that can be scrolled to the entire scroll window canvas
)

app = event(main, 1, 2, 3, 4, 5, 6, 7)
for i in range(num_events - 1):
    app.create_btn(i+1, filter)


main.mainloop()

