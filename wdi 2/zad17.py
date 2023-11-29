from math import log
        
def f(x): return ( x*log(x) - log(2020) )
def df(x): return (log(x) + 1)

x = 1
E = 0.0001
while abs(f(x)) > E :
    x = x - (f(x)/df(x))
print(x**x , x)