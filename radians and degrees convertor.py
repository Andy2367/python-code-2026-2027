'''
radiens to degrees
26-10-2025
andy cowie
'''
while True:
    ui = str(input("input 1 to convert degrees to radians or input 2 to convert radians to degrees or quit to exit: "))
    if ui == "1":
        degree = float(input("pleas input your degree value. e.g. 360: "))
        rad = 0
        if degree > 360:  # ensures that a valid value for degree in input.
            print ("sorry you can't have more that 360 degrees pleas try another value.")
        elif degree < 0:  # ensures that a valid inut is made for degree
            print ("sorry you cant have less than 0 degrees. pleas try another value.")
        else:
            rad = ((3.14/180)*degree)  # converts degree value to radians
            rad = round(rad, 3)
            print (degree, " degrees is " ,rad, " radiens")    
    elif ui == "2":
        rad_1 = float(input("pleas input your radien value: "))

        if rad_1 > 6.28318:
            print ("sorry that is an invalid input")
    elif ui == "quit":
        print ("thanks for using Andy's degree and radian converter :>")
        break