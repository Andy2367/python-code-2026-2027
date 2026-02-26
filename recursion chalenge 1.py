'''
11-09-2025
Andy Cowie
recursion chalenge
'''

def SumOfOdd(n):
    if(n==1):
        return 1
    else:
        return n+ SumOfOdd(n-2)				#call 1: 7 +  sumofodd(5)
                                            #call 2: 7 + 5 + sumoff(3)
                                            #call 3: 7 + 5+ 3 + sum(1)
'''											#call 4: 7 + 5 + 3 + 1	
while True:
    try:
        else:
            print(int(input(pleas enter a positive odd number())))
            break
    except n%2=0 or ValueError:
        print("Error Pleas enter a whole posative odd number.)
'''

#validate input for odd nums only

n=int(input("enter odd"))

while(n%2==0):	#that is an even
    n=int(input("wrong. Only odd please."))
    

print(SumOfOdd(n))	#call the function with my valid value
    
    