def iloraz_fib(a , b , E = 10**-5):
    iloraz = 1
    iloraz_s = 0.5
    while abs(iloraz_s - iloraz) > E :
        a , b = b , a+b
        iloraz_s = iloraz
        iloraz = b/a
    return iloraz

print(iloraz_fib(1 , 1))