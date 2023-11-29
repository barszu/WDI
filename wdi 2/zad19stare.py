# a = int(input())
# b = int(input())

def dz_ulam(a , b):
    if a%b == 0 : return a//b
    
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
        if r == 0 : return a/b
        
        if r not in tab_mod:
            tab_mod.append(r)
            tab_w.append(l//b)
            l = r * 10
        else:
            #szukanie w liscie ciagu powtarzajacego sie
            wynik = str(cal) + "."
            for id in range (0 , len(tab_mod)):
                start_ciagu = False
                if tab_mod[id] == r : 
                    start_ciagu = True
                    wynik += "("
                wynik += str(tab_w[id])
                
            if start_ciagu : wynik += ")"
            return wynik


print(dz_ulam(168 , 990))