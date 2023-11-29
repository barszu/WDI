def zad2(a , b):
    a = list(str(a))
    b = list(str(b))
    if len(b) > len(a) : a , b = b , a
    for i in a :
        if i not in b : 
            return "nie sa zbudowane z tych samych cyfr"
    return "sa z tych samych cyfr"

print(zad2(123 , 321))