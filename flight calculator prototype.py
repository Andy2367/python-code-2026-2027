'''
23-10-2025
Andy Cowie
flight calculator reciprocal heading
'''

curr_head = int(input("input current heading: ")) # takes current heading (will eventioly take value from aircraft/computer
rec_head = 0

if curr_head <= 180:
    rec_head = (curr_head + 180) # will add 180 to current heading when it is less than 180 (gives reciprocal heading)
    print ("reciprocal heading is ",rec_head)  # prints the reciprocal heading
elif curr_head > 180:
    rec_head = (curr_head - 180) # will take away 180 from current heading when it is more than 180 (gives reciprocal heading)
    print ("reciprocal heading is ",rec_head)  # prints the reciprocal heading
elif curr_head > 360:
    print (" invalid input") # if current heading is more than 360 (not posible) print that the input is invalid