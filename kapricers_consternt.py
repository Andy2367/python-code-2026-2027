'''
18-09-2025
Andy Cowie
6174 thing
'''
n_num = (1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999)
un_kap = int(input("pleas input a 4 diget number:" ))

while un_kap > 9999 or un_kap < 1000 or un_kap in n_num:
    print (f"Invalid input your input was {un_kap} pleas enter a posative 4 diget number with atleast one differant diget: ")
    un_kap = int(input("pleas input a 4 diget number:" ))

k = un_kap

fd = n//1000
sd = (n%1000)//100
td = ((n%1000)%100)//10
fod = (((n%1000)%100)%10)

list_k = [fd,sd,td,fod]

s_list_k+ = list_k.sort()

st_list_k = str(s_list_k)

