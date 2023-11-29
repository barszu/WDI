import sys

x = input("podaj liczbe >>>  ")
if x.isdigit():
    x = int(x)
else:
    print("bledna liczba zawiera np litere")
    sys.exit()
a = 1
b = 1

while a*b < x :
    a , b = b , a+b
if a*b == x :
    print("{0} jest iloczynem 2 kolejnych el ciagu fib {1}".format(x , (a,b)))
else:
    print("{0} nie jest iloczynem 2 kolejnych el ciagu fib".format(x))