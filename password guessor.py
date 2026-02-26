'''
8/10/015
Andy Cowie
Password guessing game
'''
p="jeff1234"
trys = 1
result = False

while trys < 4:
    up = input ("Please try to guess the password you have 3 tries. Hint: it contains a 4-letter name and 4 numbers. ")
    try:
        if up == p:
            result = True
        elif up != p:
            result = False
    except:
        print ("somthing went wrong pleas try again")
    finally:
        trysLeft = 3 - trys
        trys = trys + 1
        if not result and trysLeft > 1:
            print ("incorrect you have" ,trysLeft, "tries left")
        elif not result and trysLeft <2 and trysLeft >0:
            print ("incorrect you have" ,trysLeft, "try Left")
        elif result and trys > 1:
            print ("congrats you got the password correct in" ,trys - 1, "tries")
        elif result and trys < 2:
            print ("congrats you got the password correct in" ,trys - 1, "try")
        elif trysLeft == 0:
            print ("too many tries. please try again later")