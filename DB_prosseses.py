"""
connection to / creation of database to hold all event data
Andrew Fraser Cowie
IA
"""
import sqlite3

# function to select all records from 
def select_all(table, cur):
    cur.execute(f"SELECT * FROM {table}")
    print(cur.fetchall())

# function to add an example record to the db
def example_data(cur):
    cur.execute("""
    INSERT INTO Events (Event_name, Event_type, Location, Time, More_info)
    VALUES ("Glenco Black", 1, 1, "09-10-26", "www.example.com")
    """)

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

# make the second event have a selected value of 1(true)
cur.execute('''
UPDATE Events
SET Selected=1
WHERE Event_id = 2
''')
connection.commit()

#selects all info for selected events
cur.execute('''
SELECT *
FROM Events
WHERE Selected = 1
''')
print(cur.fetchall())
connection.commit()
connection.close()