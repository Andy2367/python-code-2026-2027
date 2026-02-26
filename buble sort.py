'''
27-10-2025
sorting notes
Andrew Cowie
'''

# buble sort

arr = ["jeff","luftwafle","goat","hola","quebec","hi","and"]
n = len(arr)
for i in range (0,n-1):
    for j in range (0,n-1-i):
        if arr[j]>arr[j+1]:  # if one is grater than the other
            arr[j],arr[j+1] = arr[j+1],arr[j]  # swap them
print (arr)
