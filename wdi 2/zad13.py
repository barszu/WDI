num = input("num  >>> ")
k = int(input("special num  >>> "))
def fun( a , uq ):
    if uq >= 9 or uq <= 0 :
        return None
    return (str(a)[-1] == str(uq))

print(fun(num , k))