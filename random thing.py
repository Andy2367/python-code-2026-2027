'''
random thing
03-11-2025
Andy Cowie
'''
import random
import time
import math

rand_nums = []
for x in range (1000):
    rand_nums.append(random.randint(1,10000))
print (rand_nums)
input()
start = time.time
def quicksort (nums):
    if len(nums) <= 1:
        return nums
    pivot = nums [0]
    rest = nums [1:]
    smaller_equal = []
    bigger = []
    for i in rest:
        if i <= pivot:
            smaller_equal.append(i)
        else:
            bigger.append(i)
    sorted_smaller_equal = quicksort(smaller_equal)
    sorted_bigger = quicksort(bigger)
    return sorted_smaller_equal + [pivot] + sorted_bigger

print (quicksort(rand_nums))
end = time.time()
time = (end - start)
print (time)
rounded = round(time,3)
print (rounded)