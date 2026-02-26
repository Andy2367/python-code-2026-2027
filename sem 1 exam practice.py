'''
sem 1 exam practice
27-11-2025
Andy Cowie
'''

data = []

with open ("driver licence data.txt", "r") as file:
    for i in file:
        parts = i.split(",")
            
        name = parts[0]
        age = parts[1]
        dl = parts[2]
            
        for i in file:
            data.append([name, age, dl])
for row in data:
    print(row)