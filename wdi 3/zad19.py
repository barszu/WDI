def is_asc(tab):
    is_asc = True
    for id in range(1,len(tab)):
        if tab[id]-tab[id-1] < 0 :
            is_asc = False
            break
    return is_asc

def sum_el(tab):
    suma = 0
    for el in tab:
        suma += el
    return suma

def zad19(tab):
    N = len(tab)
    longest = 0
    for x in range(N):
        for y in range(x , N):
            #sprawdzenie czy rosnacy ten podciag
            podciag = tab[ x : y+1 ]
            if is_asc(podciag):
                l = y-x+1
                sum_id = 0.5*(x+y)*l
                if sum_el(podciag) == sum_id :
                    longest = max(longest,l)
    return longest

print(zad19([0,1,2,3,4,5,67,7,8]))