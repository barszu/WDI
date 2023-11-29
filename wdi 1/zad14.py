def cos(x , E = 0.01):
    cos = 1.0
    factorial = 1
    i = 2
    while True:
        el = 0.0
        factorial *= i
        if i%4 == 0:
            el = (1/factorial)*(x**i)
            cos += el
        elif i%2 == 0:
            el = (1/factorial)*(x**i)
            cos -= el
        if i > 3000 : #abs(el) < E
            break
        i += 1
    return cos , i

   
print(cos(3.14/5))
