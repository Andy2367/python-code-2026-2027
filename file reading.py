'''
files
3-11-2025
Andrew Cowie
'''

data = []

with open("data.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line:
            parts = line.split(",")		#this will put 	"name: <name>" in position [0] etc.
            
        name = parts[0].split(":")[1].strip()	#this will split by : so name goes to [1]
        score = parts[1].split(":")[1].strip()	#same thing for score.
        
        data.append([name,score])
        print(data)
print (f"{'name':<20} {'score':<15}")
print ("-"*50)
for row in data:
    print (f"{row[0] : <20} {row[1] : <15}")

data1 [0][0] = "Matteo porrera"
with open("data.txt", "w") as file:
    for r in data1:
        