from math import sqrt
E = 0.0000001
p = sqrt(0.5)
a = p
b = sqrt(0.5 + (0.5 * p))
iloczyn = a*b
while b > E + 1 :
    a , b = b , sqrt(0.5 + (0.5 * a))
    iloczyn *= b
    print("compiling")
pi = 2/iloczyn
print(pi)