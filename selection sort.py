'''
selection sort
31-10-2025
Andrew Cowie
'''
import random
import time
arr = []  # array
for x in range (1,1000):   # for lenth of array
    arr.append(random.randint(1,1000))  # add random numbers to each index in the array
print (arr) # print array
input()
s = time.time()
for i in range(len(arr)):  # for lenth of array
    min_pos = i  # asumes each position is the smalest
    for j in range(i+1,len(arr)):   # for lenth of array
        if (arr[j] < arr[min_pos]):
            min_pos = j  # make the new minimum
    if (min_pos != i):  # if the 2 position values don't match
        arr[i],arr[min_pos] = arr[min_pos],arr[i]
e = time.time()
t = (e-s)
print (arr)
print ("it took",t,"seconds")