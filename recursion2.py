'''
fibanaci recursion
18-09-2025
Andy Cowie
'''

def f(n):
    if n <=1:
        return n
    else:
        return f(n-1) + f(n-2)
while True:
    print(f(int(input())))