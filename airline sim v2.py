'''
airline sim v2
Andrew Cowie
started 7-11-2025
'''

import time
import random

flights = [
    [0, 50, 0],
    [0, 100, 0],
    [0, 200, 0]
    ]


#micalanious
quit_ = False
total_m = (short_m + med_m + long_m)
cash = round(100, 0)

def short (flights):
    if 


        none
info = []  # will hond arr for info doc

while quit_ == False:
    print (f"you have {total_m} aircraft in maintanaince")
    print (f"you have {cash} credits")
    print ("what would you like to buy")
    print (f"1 for short hall plane {short_price} credits")
    print (f"2 for medium hall plane {med_price} credits")
    print (f"3 for long hall plane {long_price} credits")
    user_choice = int(input())
    if user_choice.strip().lower == "quit":
        print ("thanks for playing :>")
        break
    elif user_choice == 1:
        if (cash - short_price) < 0:
            print ("sorry you don't have enough credits to buy this aircraft")
        else:
            short = (short + 1)
            cash = (cash - short_price)
            short_price = round((short_price * 1.5), 0)
            print (f"you have {short} short hall planes")
            print (f"you have {cash} credits")

    elif user_choice == 2:
        if (cash - med_price) < 0:
            print ("sorry you dont have enough credits to buy this aircraft")
        cash = (cash - med_price)
        med = (med + 1)
        med_price = round((med_price * 1.5), 0)
        print (f"you have {med} medium hall planes")
        print (f"you have {cash} credits")

    elif user_choice == 3:
        if (cash - long_price) < 0:
            print ("sorry you don't have enough credits to buy this aircraft")
        else:
            cash = (cash - long_price)
            long = (long + 1)
            long_price = round((long_price * 1.5), 0)
            print (f"you have {long} long hall planes")
            print (f"you have {cash} credits")
    time.sleep(3)