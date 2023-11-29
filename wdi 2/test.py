def to_power(x , y):
    wynik = 1
    notacja = 0
    for _ in range(y):
        wynik *= x
        len_wynik = len(str(wynik))
        if len_wynik > 9 :
            len_end = len_wynik - 5
            notacja += len_end
            wynik = round(wynik , -1*len_end)
        print(wynik , notacja)
    return (wynik , notacja) 

print(to_power(2020 , 2020))
