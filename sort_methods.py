import random as rnd
import time

a = []
for i in range(1,100000):
    a.append(i)
    
b = [2,4,5,3,7,1,9,10,8,6]
def randomise(a):
    for i in range(len(a)):
        r1 = rnd.randint(0,len(a)-1)
        r2 = rnd.randint(0,len(a)-1)
        a[r1], a[r2] = a[r2], a[r1]
    return a

def ss(a):
    for i in range(len(a)):
        min_idx = i
        for j in range(i+1, len(a)):
            if a[min_idx] > a[j]:
                min_idx = j
        if(min_idx!=i):
            a[i], a[min_idx] = a[min_idx], a[i]
    return a

def quick(a):
    if len(a) <= 1:
        return a
    else:
        pivot = a[0]
        rest = a[1:]
        
        soe = []
        b = []
        
        for i in rest:
            if i <= pivot:
                soe.append(i)
            elif i > pivot:
                b.append(i)
    sorted_smaller = quick(soe)
    sorted_bigger = quick(b)
    return sorted_smaller + [pivot] + sorted_bigger


def buble(a):
    for i in range(len(a)):
        if i > i+1:
            

print(randomise(a))
print()
print("enter the sort that you would like to use")
print("ss for selection sort")
print("qs for quick sort")
print("e to end the program")
print()

end = False
while end == False:
    i = input().strip().lower()
    
    if i == "e":
        end = True
        print("Exiting program. Have a good day. :)")
    
    elif i == "ss":
        print("Sorting. Pleas be pacient")
        s = time.time()
        print(ss(a))
        e = time.time()
        t = e - s
        print(f"it took {t:.6f} seconds")
    elif i == "qs":
        print("Sorting. Pleas be pacient")
        s = time.time()
        print(quick(a))
        e = time.time()
        t = e - s
        print(f"it took {t:.6f} seconds")
