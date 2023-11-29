num = input(">>> ")
l = len(num)
condition = False
for cyfra in num :
    if int(cyfra) == l :
        condition = True
        break
if condition :
    print("{0} zawiera cyfre ktora jest dlugoscia liczby".format(num))
else:
    print("{0}  NIE zawiera cyfry ktora jest dlugoscia liczby".format(num))
