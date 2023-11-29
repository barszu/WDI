#e = 1 + 1/1! + 1/2! + 1/3! ...
E = 0.00001
e = 1
silnia = 1
i = 1
el = 1
while el > E:
    silnia *= i 
    el = 1/silnia
    e += el
    i += 1
print(e)