from prettytable import PrettyTable

arr = PrettyTable()
arr.feild_names = ["yo","lo"]


with open ("data.txt", "r") as file:
    for line in file:
        arr.append(line)
        
print (arr)