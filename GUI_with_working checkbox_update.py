import tkinter as tk
import sqlite3

# function to select all records from 
def select_all(table, cur):
    cur.execute(f"SELECT * FROM {table}")
    print(cur.fetchall())

# function to add an example record to the db
def example_data(cur):
    cur.execute("""
    INSERT INTO Events (Event_name, Event_type, Location, Time, More_info)
    VALUES (?, ?, ?, ?, ?)""", ("Glenco Black", 1, 1, "09-10-26", "www.example.com"))

# connect to database or crerate one if it does not exist
connection = sqlite3.connect("IA_database.db")
cur = connection.cursor()

# create all requierd tables if they don't exist

c1 = """CREATE TABLE IF NOT EXISTS
Events(Event_id INTEGER PRIMARY KEY,
Event_name TEXT,
Event_type INTEGER,
Location INTEGER,
Time DATETIME,
More_info TEXT,
Selected INTEGER NOT NULL DEFAULT 0 CHECK(SELECTED IN (0,1)))""" # BOOL data type needs fixed.

c2 = """CREATE TABLE IF NOT EXISTS
Locations(location_id INTEGER PRIMARY KEY,
location_name TEXT)"""

c3 = """CREATE TABLE IF NOT EXISTS
Event_types(type_id INTEGER PRIMARY KEY,
type_name TEXT)"""

cur.execute(c1) # creates Events table
cur.execute(c2) # creates Locations table
cur.execute(c3) #creates Event type table

connection.commit() # saves changes to the db (should be added alfter evry block of executes for redundency)

example_data(cur)
example_data(cur)
example_data(cur)
connection.commit()

def update_status():
    conn = sqlite3.connect("IA_database.db")
    cur = conn.cursor()
    cur.execute("SELECT Selected FROM Events WHERE Event_id IS 1")
    print(cur.fetchall())
    cur.execute("SELECT Selected FROM Events WHERE Event_id IS 1")
    status = cur.fetchone()
    print(status)
    if status[0] == 1:
        cur.execute("UPDATE Events SET Selected = 0")
        conn.commit()
        select.config(bg="red")
        print("condition 1")
    elif status[0] == 0:
        cur.execute("UPDATE Events SET Selected = 1")
        conn.commit()
        select.config(bg="blue")
        print("condition 2")
    else:
        print("condition 3")
    cur.execute("SELECT Selected FROM Events WHERE Event_id IS 1")
    print(cur.fetchall())

cur.execute("SELECT selected FROM Events WHERE Event_id = 1")
cur.fetchall()

cur.execute("SELECT selected FROM Events WHERE Event_id = 1")
status = cur.fetchone()

main = tk.Tk()
main.geometry("500x500")
if status[0] == 0:
    select = tk.Button(text=status, command=update_status, bg="red")
    select.pack(pady=10)
elif status[0] == 1:
    select = tk.Button(text=status, command=update_status, bg="blue")
    select.pack(pady=10)
    print("error")

tk.Label(text=status).pack()
main.mainloop()
