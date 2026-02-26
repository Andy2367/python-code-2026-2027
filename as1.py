'''
airline sim v1
Andrew Cowie
started 5-11-2025
'''
import time
import multiprocessing
import random
cash = round(100, 0)
short = 0
short_price = round(50, 0)
short_m = 0
short_sleep = 5
med = 0
med_price = round(100, 0)
med_sleep = 15
long = 0
long_price = round(200, 0)
long_sleep = 30
quit_ = False

def short_flights(sf):
    time.sleep(short_sleep)
    sm = random.randint(0,100)
    if short_m >= 1:
        short_m - 1
    elif sm <= 40:
        short_m + 1
    else:
        nothing
    cash + (5 * (short - short_m))

def med_flights (mf):
    time.sleep(med_sleep)
    cash + (15 * med)

def long_flights(lf):
    time.sleep(long_sleep)
    cash + (50 * long)
info = []  # will hond arr for info doc

while quit_ == False:
    print (f"you have {cash} credits")
    print (f"what would you like to buy")
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