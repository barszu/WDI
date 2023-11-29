def zad14(N , testy):
    from random import randint
    c = 0
    for t in range(testy):
        y = [0]*365
        for p in range(N):
            b = randint(0,364)
            if y[b] > 1 :
                c += 1
                break
            else:
                y[b] += 1
    return c/testy

print(zad14(210 , 10000))