'''
airline sim v3
Andrew Cowie
8-11-2025
'''

import time
import random

flights = [
    [0, 50, 0],  # short
    [0, 100, 0], # medium
    [0, 200, 0], # long
    [100],       #credits
    ]

quit_ = False
info = []  # will hond arr for info doc

with open ("airline sim info.txt", "r") as file:
    for line in file:
        row = line
        info.append(row)

def short_1 (flights):
    if random.randint (0,100) <= 20:
        flights[0][2] += 1
    else:
        pass
    return flights


def short (flights):
    if flights [0][2] > 0:
        flights[0][2] -= 1
    else:
        pass
    return flights

def med_1 (flights):
    if random.randint (0,100) <= 30:
        flights[1][2] += 1
    else:
        pass
    return flights


def med (flights):
    if flights [1][2] > 0:
        flights[1][2] -= 1
    else:
        pass
    return flights

def long_1 (flights):
    if random.randint (0,100) <= 40:
        flights[2][2] += 1
    else:
        pass
    return flights

def long (flights):
    if flights [2][2] > 0:
        flights[2][2] -= 1
    else:
        pass
    return flights

def money(flights):
    if flights[0][0] > 0:
        flights[3][0] += (20*(flights[0][0] - flights[0][2]))
    elif flights[1][0] > 0:
        flights[3][0] += (35*(flights[1][0] - flights[1][2]))
    elif flights[2][0] > 0:
        flights[3][0] += (50*(flights[2][0] - flights[2][2]))
    else:
        pass
    return flights

def flights_():
    short(flights)
    short_1(flights)
    med(flights)
    med_1(flights)
    long(flights)
    long_1(flights)
    money(flights)
    return flights

while quit_ == False:
    try:
        print (f"you have {flights_()[3][0]} credits")
        time.sleep(2)
        print()
        print ("what would you like to do")
        print (f"1. buy a short hall plane {flights[0][1]} credits")
        print (f"2. buy a medium hall plane {flights[1][1]} credits")
        print (f"3. buy a long hall plane {flights[2][1]} credits")
        print ("4. do nothing")
        print ("to end input(quit)")
        print ("to see the sim info input(info)")

        user_choice = input()
        choice = user_choice.strip().lower()
        if choice == "info":
            for i in info:
                print (i)
            go = input()
        elif choice == "quit":
            print()
            print ("thanks for playing :>")
            break
        elif int(choice) == 1:
            if flights[3][0] - flights[0][1] < 0:
                print()
                print ("sorry you don't have enough credits to buy this aircraft")
            else:
                flights[0][0] += 1
                flights[3][0] -= flights[0][1]
                flights[0][1] *= 1.5
                print()
                print (f"you have {flights[0][0]} short hall planes")
                print (f"you have {round(flights[3][0], 2)} credits")

        elif int(choice) == 2:
            if flights[3][0] - flights[1][1] < 0:
                print()
                print ("sorry you dont have enough credits to buy this aircraft")
            flights[1][0] += 1
            flights[3][0] -= flights[1][1]
            flights[1][1] *= 1.5
            print()
            print (f"you have {flights[1][0]} medium hall planes")
            print (f"you have {round(flights[3][0], 2)} credits")

        elif int(choice) == 3:
            if flights[3][0] - flights[2][1] < 0:
                print()
                print ("sorry you don't have enough credits to buy this aircraft")
            else:
                flights[2][0] += 1
                flights[3][0] -= flights[2][1]
                flights[2][1] *= 1.5
                print()
                print (f"you have {flights[2][0]} long hall planes")
                print (f"you have {round(flights[3][0], 2)} credits")
        else:
            pass
        time.sleep(3)
        if flights_()[0][0] or flights_()[1][0] or flights_()[2][0] > 0:
            print()
            print ("you receaved income from your planes")
            time.sleep(2)
    except:
        print("sorry somthing went rong pleas try again")
        time.sleep(2)