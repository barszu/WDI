def zad18(t):
    n = len(t)
    longest = 0
    # x y to id/ wskazniki
    for x in range(n):
        for y in range(x+1 , n):
            flag = True
            dl_p = y-x+1
            # y - x + 1 - dlugosc podciagu 
            for i in range(dl_p):
                #sprawdzenie czy jest palidromem
                if t[x+i] != t[y-i] or t[x+i]%2 == 0:
                    flag = False
                    break
            if flag: longest = max(longest,dl_p)
    return longest