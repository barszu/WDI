def tab_gen(N):
    import random
    tab_N = [0]*N
    for id in range(N):
        tab_N[id] = random.randint(100 , 999)
    return tab_N

def zawiera(tab , tab_mala):
    zawiera = False
    for id in range(len(tab)):
        if tab[id] == tab_mala[0]:
            id_shift = id
            break
    if tab[id_shift : id_shift + len(tab_mala)] == tab_mala :
        zawiera = True
    return zawiera

def zad13(tab):
    N = len(tab)
    longest = 0
    for x in range(N):
        for y in range(x , N):
            podciag = tab[x:(y+1)]
            rewers = podciag[::-1]
            if zawiera(tab , rewers) :
                l = y - x + 1
                longest = max(longest , l)
    return longest

t = [2,9,3,1,7,11,9,6,7,7,1,3,9,12,15]
print(zad13(t))
