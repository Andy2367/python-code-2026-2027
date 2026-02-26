'''
30-10-2025
quick sort
Andrew Cowie
'''
import random

nums = []
for i in range(1,6700):
    nums.append(random.randint(500,1000)) # nums = random numbers
print (nums)
    
def quicksort(nums):  # function defined
    if len(nums)<= 1:  # if nums is shorter or the 1 in lenth
        return nums # return the array
    
    pivot = nums[0]  # makes the first index the pivot
    rest = nums[1:]  # all other data
    
    small_eq = [] # lists of smaller or equal values to pivot
    bigger = []  # list of larger values than pivot
    
    for x in rest:  # for loop with duration of lenth of list rest
        if x <= pivot:  # if the value is less than ore equal to pivot
            small_eq.append(x) # add the value to the list for samller or equal values
        else: # if not
            bigger.append(x) # add data to bigger
            
    sorted_small = quicksort(small_eq) # makes small_eq the the arr in quicksort
    sorted_bigger = quicksort(bigger) # dose the same for bigger list
    
    return sorted_small + [pivot] + sorted_bigger # compines all of the lists
input ()
S_data = quicksort(nums)
print (S_data)