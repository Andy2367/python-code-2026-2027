'''
judo radomiser
'''

import random as rnd

a = [1,2,3,4,5,6,7,8,9,10]

def randomiser(a):
    for i in range(len(a)):
        r1 = rnd.randint(0,len(a)-1)
        r2 = rnd.randint(0,len(a)-1)
        a[r1], a[r2] = a[r2], a[r1]
    return a

print (a)


for i in range(0, int(input("input the amount of times you would like to randomise the list. eg. 10: "))):
    print()
    print(randomiser(a))