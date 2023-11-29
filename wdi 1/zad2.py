def fib(a , b , do):
    while a + b < do :
        a , b = b , a+b
    if a+b == do :
        return do
    else: 
        return b

import sys
a0 = 1
b0 = 1
do = 2022

while a0 + b0 <= do :
    if fib(a0,b0,do) == do :
        print("poczatkowe liczby to {0} {1}".format(a0 , b0))
        sys.exit()
    else:
        a0 += 1
        b0 += 1
else:
    print("bruh nic")
        






# rok = 2022
# a0 = 1
# b0 = 1
# a = a0
# b = b0
# condition = True
# while condition :

#     while (a + b) <= rok :
#         a , b = b , a+b
#     if b != rok :
#         a = a0 + 1
#         b = b0 + 1
#     elif b == rok :
#         break
#         condition = False
#     print(a , b)
# print("wyniki to {0}{1}".format(a , b))
    