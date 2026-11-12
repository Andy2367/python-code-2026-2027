import tkinter as tk
import sqlite3

class myclass():
    def __init__(self, root, a, b, c):
        self.root = root
        self.a = a
        self.b = b
        self.c = c
        self.btns = {}

    def create_btn(self, ID):

        conn = sqlite3.connect("IA_database.db")
        cur = conn.cursor()
        cur.execute(f"SELECT Event_name FROM Events WHERE Event_id = {ID}")
        name = cur.fetchone()
        name = name[0]

        cur.execute(f"SELECT Event_type FROM Events WHERE Event_id = {ID}")
        e_type = cur.fetchone()
        e_type = e_type[0]

        cur.execute(f"SELECT Location FROM Events WHERE Event_id = {ID}")
        loc = cur.fetchone()
        loc = loc[0]

        cur.execute(f"SELECT Time FROM Events WHERE Event_id = {ID}")
        time = cur. fetchone()
        time = time[0]

        cur.execute(f"SELECT More_info FROM Events WHERE Event_id = {ID}")
        info = cur.fetchone()
        info = info[0]

        cur.execute(f"SELECT Selected FROM Events WHERE Event_id = {ID}")
        status = cur.fetchone()
        status = status[0]

        date = "--date--"

        Text = f"{name} {e_type}, in {loc}, at {time}, on {date}, get more info at {info}"
        
        btn = tk.Button(root, text=Text)
        self.btns[ID] = btn
        btn.pack()



root = tk.Tk()

app = myclass(root, 1, 2, 3)
for i in range(3):
    app.create_btn(i+1)

root.mainloop()