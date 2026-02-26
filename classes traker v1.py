'''
ATC classes tracker v3
Andy Cowie
14-11-2025
'''
import time

first = []

leading = []

senior = []

master = []

compleat = []

menu1 = [
    ["1"," see a class"],
    ["2"," see everyone"],
    ["3"," surch for somthing"]
    ]

class_menu = [
    ["1."," first class"],
    ["2."," leading"],
    ["3."," senior"],
    ["4."," master"]
    ]

surch_menu = [
    ["1"," surch for a name"],
    ["2"," surch for a subject"]
    ]

end = False

while end == False:
    print("Hi welcome to the classes tracker. This program is designed to alow you to track what class someone is in, what subject they are learning and have learned, and how far throgh a subject they are.")
    time.sleep(1)
    for line in menu1:
        print(line)
    choice = int(input())
    
    if choice == 1:
        for row in class_menu:
            print(row)
        choice = int(input())
        if choice == 1:
            for row in first:
                print(row)
        elif choice == 2:
            for row in leading:
                print(row)
        elif choice == 3:
            for row in senior:
                print(row)
        elif choice == 4:
            for row in master:
                print(row)
    elif choice == 2:
        for row in first:
            print (row)
        for row in leading:
            print(row)
        for row in senior:
            print(row)
        for row in master:
            print(row)
        for row in compleat:
            print (row)