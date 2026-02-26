'''
12-09-2025
Andy Cowie
notes:

recursion = factorial (plate stack) (FIRST IN == LAST OUT)
'''


def fact(n):
    if (n == 1):
        return 1
    else:
        return n*fact(n-1)
while True:
    try:
        print(fact(int(input())))
    except ValueError:
        print ("error")
        
        
