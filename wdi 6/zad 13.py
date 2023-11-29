def zad13(num):
    T = []
    def engine(p,a,wynik=[]):
        nonlocal T
        if p <= 0 or p == a: 
            # T += wynik
            return 
        wynik += [a]
        if p-a >= 0:
            T += [wynik+[p-a]]
        return engine(p-a,a, wynik)
    
    for a in range(1, num//2 + 1): #a - start num
        engine(num,a,[])
        
    return T

print(zad13(3))

#inna wersja zadania - moje lepsze :)
def print_splits(num :int ,j:int , split: list[int]):
    if num == 0 :
        print(split)
        return
    
    if j == 0: mini = 1
    else: mini = split[j-1]
    
    for i in range(mini , num+1):
        split[j] = i
        print_splits(num - i , j + 1 , split)
        split[j] = 0

print(print_splits(4,0,[0]*4))