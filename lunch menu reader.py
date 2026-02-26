'''
lunch menu reader
Andy Cowie
14-11-2025
'''
menu = []
with open ("menu.txt", "r") as file:
    for row in file:
        row = row.strip()
        menu.append(row)
for i in menu:
    print(i)
    
while True:
    print("what dish would you like to find")
    for line in choice:
        print(*line)