global T

# from random import randint
# T = [ [0]*8 for _ in range(8) ]
# for x in range(8):
#     for y in range(8):
#         T[x] [y] = randint(10,99)
# for _ in range(8): print(T[_])
T = [[43, 93, 34, 57, 90, 23, 81, 57],[84, 18, 48, 45, 24, 34, 95, 31],[15, 43, 92, 41, 35, 97, 60, 24],[47, 83, 49, 11, 34, 77, 14, 76],[86, 61, 25, 99, 84, 77, 85, 73],[92, 45, 65, 69, 72, 80, 69, 99],[51, 37, 31, 62, 11, 88, 62, 80],[29, 86, 80, 19, 59, 70, 42, 58]]
#---------------------------------------------
def ending(num): #koncowka liczby cyfra
    return num%10

def begin(num): #poczatek liczy cyfra
    from math import log10
    n = int(log10(num))
    return num//(10**n)


def canIfn(w,k,old_ending:int):
    if w >= 8 or k >= 8 : return False
    #jestesmy w planszy przy tym ruchu
    new_begin = begin(T[w] [k])
    if old_ending < new_begin : return True
    return False
    



def rek(w,k,canI_be_here): 
    # z tresci wynika ze krol stoi na polu o indeksie [0][0] i moze sie poruszac tylko w dol w prawo i po przekatnej (w prawy dolny rog)
    # canI_be_here - true / false -> czy moze byc na tym polu -> uruchamia sie sprawdzenie
    if not canI_be_here: return False
    if w == 7 and k == 7 : return True
    
    return rek(w,k+1,canIfn(w,k+1,ending(T[w] [k]))) or rek(w+1,k,canIfn(w+1,k,ending(T[w] [k]))) or rek(w+1,k+1,canIfn(w+1,k+1,ending(T[w] [k])))
    #               w prawo                                             w dol                                 po przekatnej
    "TODO zapisz te waruny jakos w petli zeby taka sama ich interpretacja byla flagi???"
    
    
def rek2(w,k):
    if w == 7 and k == 7: return True
    
    for (dw , dk) in [(1,1),(1,0),(0,1)]:
        if canIfn(w+dw , k+dk , ending(T[w] [k])) :
            return rek2(w+dw,k+dk)
    return False
    
    
    
print(rek(0,0,True))
print(rek2(0,0))