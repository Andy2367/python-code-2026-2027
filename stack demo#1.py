'''
06-10-2025
satcks and stack functions
Andy Cowie
'''

nic = []
finish = "done"
while True:
    u_input = input("incert a class members name or done to finish: ")
    if u_input == finish:
        print(nic)
        print(nic.pop())  # gets rid of "Andy"
        print(nic.pop())  # gets rid of "Karim"
        print(nic)
        break
    else:
        nic.append(u_input)