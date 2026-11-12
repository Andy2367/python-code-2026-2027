import sqlite3
import tkinter as tk

class event:
    def __init__(self, main, id, name, event_type, location, event_time, more_info, selected):
        self.id = int(id)
        self.name = name
        self.event_type = event_type
        self.location = location
        self.event_time = event_time
        self.more_info = more_info
        self.selected = selected
        self.main = main
        self.btns = {}

    def update_status(self):
        conn = sqlite3.connect("IA_database.db")
        cur = conn.cursor()
        cur.execute(f"SELECT Selected FROM Events WHERE Event_id IS {self.id}")
        print(cur.fetchall())
        status = self.get_status()
        print(status)
        if status[0] == 1:
            cur.execute(f"UPDATE Events SET Selected = 0 WHERE   Event_id IS {self.id}")
            conn.commit()
            select.config(bg="red")
            print("condition 1")
        elif status[0] == 0:
            cur.execute(f"UPDATE Events SET Selected = 1 WHERE Event_id IS {self.id}")
            conn.commit()
            select.config(bg="blue")
            print("condition 2")
        else:
            print("condition 3")
        cur.execute(f"SELECT Selected FROM Events WHERE Event_id IS {self.id}")
        print(cur.fetchall())
        conn.close()

    def get_status(self):
        conn = sqlite3.connect("IA_database.db")
        cur = conn.cursor()
        cur.execute(f"SELECT Selected FROM Events WHERE Event_id IS {self.id}")
        status = cur.fetchone()
        conn.close()
        return status
    
    def create_widget(self, name):
        btn = tk.Button(main, text=name)
        self.btns[name] = btn
        btn.pack()

def create_obj(ID):
    conn = sqlite3.connect("IA_database.db")
    cur = conn.cursor()

    cur.execute(f"SELECT Event_id FROM Events WHERE  Event_id = {ID}")
    id = cur.fetchone()
    id = id[0]

    cur.execute(f"SELECT Event_name FROM Events WHERE  Event_id = {ID}")
    name = cur.fetchone()
    name = name[0]

    cur.execute(f"SELECT Event_type FROM Events WHERE  Event_id = {ID}")
    event_type = cur.fetchone()
    event_type = event_type[0]

    cur.execute(f"SELECT Location FROM Events WHERE  Event_id = {ID}")
    loc = cur.fetchone()
    loc = loc[0]

    cur.execute(f"SELECT Time FROM Events WHERE  Event_id = {ID}")
    time = cur.fetchone()
    time = time[0]

    cur.execute(f"SELECT More_info FROM Events WHERE  Event_id = {ID}")
    more_info = cur.fetchone()
    more_info = more_info[0]

    cur.execute(f"SELECT Selected FROM Events WHERE  Event_id = {ID}")
    status = cur.fetchone()
    status = status[0]

    app = event(id, main, name, event_type, loc, time, more_info, status)
    return app

main = tk.Tk()
main.geometry("250x300")
