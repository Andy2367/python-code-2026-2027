'''
25-09-2025
Andy Cowie
surching / quick surch
'''

'''
linier surch = in a line long time

binery surch = takes off chunks and disregards non needed (data must be sorted first)
'''

# linier

def linear_surch(arr, target):       # function to find target
    for index in range(len(arr)):
        if arr[index] == target:
            return index
        else:
            return -1 # not found

arr = [10, 25, 30, 45, 50]  # array containing target
target = int(input("pleas input a number to find if it is in the list: "))# target to be found

result = linear_surch(arr, target)  # calls function and becomes result
if result != -1:
    print ("found in index",result)  # if target found print the location of the target
else:
    print ("Element not found")  # if target nopt found print element not found
    

# recursive

def rec_surch(arr, target, index):   # recursive function for surching for target
    if index == len(arr):
        return -1                # not found
    if arr[index] == target:
        return rec_surch(arr, target, index +1)

result1 = rec_surch(arr, target, 0) # calls the recursive function
if 

# binary

low = 0
high = len(arr)
mid = (low + high)//2

def Bin_surch(low, high, mid):
    while (low <= high):
        if (arr[mid]==target):  # if the target is at the mid point return the position of the target
            return mid
        if (target > arr[mid]):  # if the target is more than the value of the mid point make low the mid point + 1
            low = mid +1
        if (target < arr[mid]): # oposit of perveos if condition
            high = mid -1
        mid = (low + high)//2 # calculates the mid point
        
result2 = Bin_surch(low, high, mid)  # calls the binery function
if mid == target:
    print ("position of your number is", mid)





