def rek(tab,start,iloczyn):
    suma = 0
    for i in range(start,len(tab)):
        suma += iloczyn*tab[i]
        suma += rek(tab,i+1,iloczyn*tab[i])
    return suma

print(rek([2,3,5] , 0 , 1))