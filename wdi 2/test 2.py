a , b = 168 , 990
import sys

if a%b == 0 : 
    print(a//b)
    sys.exit()

if a < 0 or b < 0 : 
    is_pos = False
    a = abs(a)
    b = abs(b)
else:
    is_pos = True

l = a
cal = a//b
if cal > 0 : l = l - (cal*b)

tab_mod = []
tab_w = []
l *= 10
while True :
    r = l%b
    
    if r == 0 : 
        print (a/b)
        sys.exit()
    
    if r in tab_mod:
        tab_w.append(l//b)
        tab_mod.append(r)
        #szukanie w liscie ciagu powtarzajacego sie
        wynik = str(cal) + "."
        start_ciagu = False
        for id in range (0 , len(tab_mod)):
            if tab_mod[id] == r :
                #blad wstawiania nawiasow
                start_ciagu = True
                wynik += "("
            wynik += str(tab_w[id])
            
        if start_ciagu : wynik += ")"
        print(wynik)
        sys.exit()
        
    
    tab_w.append(l//b)
    tab_mod.append(r)
    l = r * 10