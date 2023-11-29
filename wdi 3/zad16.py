def bubble_sort(tab):
    sort_cond = True
    while sort_cond:
        sort_cond = False
        for id in range(len(tab)-1):
            if tab[id+1] < tab[id]:
                tab[id+1] , tab[id] = tab[id] , tab[id+1]
                sort_cond = True
    return tab

def zad16(tab):
    n = len(tab)
    
print(bubble_sort([6 ,9 ,10, 7 ,99 , 100 ,12121]))
