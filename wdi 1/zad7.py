innum = int(input("please insert number >>> "))
a = 1
b =1
while a*b < innum + 1 :
    if a*b == innum :
        print("{0} jest w ciagu fib ".format(innum))
    a , b = b , a+b