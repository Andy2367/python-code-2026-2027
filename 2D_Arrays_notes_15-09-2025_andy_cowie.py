'''
15-09-2025
Andy Cowie
2D arrays
'''

wify_data = [
            [0,0,2,12,70,79,99],         # array of data row = day colum = time(12:00 - 06:00)
            [21,13,2,3,50,67,69],
            [1,3,4,67,90,101,240],
            [0,0,7,8,45,391,308],
            [499,580,0,0,0,0,0],
            [12,13,11,295,55,67,87],
            [28,301,245,275,8267,444,0]
]

max_v = wify_data[0][0]   # highest value variable
max_d = 0                  # day variable
max_t = 0                 # time variable

for row in range(0,7):                     # outer loop for checking the highest number
    for col in range(0,7):                    # inner loop for checking the highest number
        if (wify_data [row][col]>max_v):          # if the number id higher than perviouse high in the index array asighns the highest number to max_v
            max_v = wify_data [row][col] 
            max_d = row
            max_t = col


print(max_v)  # prints the higest number

days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]                 # lsit of days
times = ["12:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00"]    # list of times

print(days[max_d], times[max_t])     # prints the day and tiem of the highest number

# sums data for each day

d1 = sum (wify_data[0])
d2 = sum (wify_data[1])
d3 = sum (wify_data[2])
d4 = sum (wify_data[3])
d5 = sum (wify_data[4])
d6 = sum (wify_data[5])
d7 = sum (wify_data[6])