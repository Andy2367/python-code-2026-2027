'''
coord decrypt
andy and matteo
12-09-2025
'''
while True:
    c1 = input("pleas input the first coordanate eg...(0,0) ")
    c2 = input("Pleas input the secpond coordanate eg...(0,0) ")
    try:
        s1 = c1.split(",")  # splits at the comas
        s2 = c2.split(",")

        x1 = float(s1[0])
        y1= float(s1[1])
        x2 =float(s2[0])
        y2=float(s2[1])

        x_mid = (x1+x2)/2
        y_mid = (y1+y2)/2

        midpoint = (x_mid,y_mid)

        print(f" The midpoint is {midpoint}")
        break
    except:
        print("somthing went wrong pleas try again later")
    finally:
        print (":>")
