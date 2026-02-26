'''
airline sim v5
Andrew Cowie
13-11-2025
'''
# use sort to determin lowest price and then do an if the money you have is less than the lowest price dont give the
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
intro = "Hi wellcome to the airline simulator. in this simulator you build your own airline and try to maxemise profits. to see your airline data at any time press 'd'. I hope that you enjoy the game pleas enjoy.  :>"

with open ("airline sim info.txt", "r") as file:
    for line in file:
        info.append(line)

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
print (intro)
time.sleep(3)
while quit_ == False:
    #try:
        print()
        print (f"you have {flights_()[3][0]} credits")
        time.sleep(2)
        print() # blank line
        print ("what would you like to do")
        print (f"s. buy a short hall plane {flights[0][1]} credits")
        print (f"m. buy a medium hall plane {flights[1][1]} credits")
        print (f"l. buy a long hall plane {flights[2][1]} credits")
        print ("x. do nothing")
        print ("q. to save and end the game")  # writes game data to file and leaves
        print ("i. to see the game info") # prints info file
        print ("d. to see your airline data") # oppens file and prints it

        user_choice = input()
        choice = user_choice.strip().lower()
        if choice == "i":
            for i in info:
                print (i) # not working!!!!!
            go = input()
        elif choice == "q":
            print() # blank line
            print ("thanks for playing :>")
            break
        elif choice == "s":
            if flights[3][0] - flights[0][1] < 0:
                print() # blank line
                print ("sorry you don't have enough credits to buy this aircraft")
            else:
                flights[0][0] += 1
                flights[3][0] -= flights[0][1]
                flights[0][1] *= 1.5
                print() # blank line
                print (f"you have {flights[0][0]} short hall planes")
                print (f"you have {round(flights[3][0], 2)} credits")

        elif choice == "m":
            if flights[3][0] - flights[1][1] < 0:
                print() # blank line
                print ("sorry you dont have enough credits to buy this aircraft")
            flights[1][0] += 1
            flights[3][0] -= flights[1][1]
            flights[1][1] *= 1.5
            print() # blank line
            print (f"you have {flights[1][0]} medium hall planes")
            print (f"you have {round(flights[3][0], 2)} credits")

        elif choice == "l":
            if flights[3][0] - flights[2][1] < 0:
                print() #blank line
                print ("sorry you don't have enough credits to buy this aircraft")
            else:
                flights[2][0] += 1
                flights[3][0] -= flights[2][1]
                flights[2][1] *= 1.5
                print() #blank line
                print (f"you have {flights[2][0]} long hall planes")
                print (f"you have {round(flights[3][0], 2)} credits")
            
        else:
            pass
        time.sleep(3)
        if flights_()[0][0] >0 or flights_()[1][0] >0 or flights_()[2][0] > 0:
            print() # balnk line
            print ("you receaved income from your planes")
            time.sleep(2)
    #except:
        #print("sorry somthing went rong pleas try again")
        #time.sleep(2)
