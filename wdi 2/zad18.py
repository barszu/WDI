#a0 , a1 = 0 , 1 #a2 = a1 - (b1 * a0)
#b0 = 2 #b1 = b0 + 2*a0
# def zad18():
#     a0 = 0
#     a1 = 1
#     b0 = 2
#     b1 = 2
    
#     id = 1
    
#     while a1 < num:
#         num = int(input(" wpisz wyraz ciagu a  >>>  "))
#         if num == a0 : 
#             print(b0) 
#         if num == a1 :
#             print(b1)
#         id += 1
#         #if id >= 3 : 
#         a1 , a0 = a1 - (b1 * a0) , a1
#         b1 = b1 + 2*a1
#         print(a0 , a1 , b1)

# zad18()
















id = 0
a = 0
b = 2
while True:
    num = int(input(" wpisz wyraz ciagu a  >>>  "))
    #znalezienie od ktorego id - wyrazu zaczyna sie ciag a - sprawdzenie poprawnosci danych z input
    while a != num and abs(a) <= abs(num) :
        #przypadek szczegolny dla id = 0
        if id == 0 :
            ap = a
            a , b = 1 , b+ 2*a
            id += 1
            continue
        
        ap = a
        a , b = a - (b*ap) , b + 2*a
        
        id += 1

    if num == a : print(b)
    else: 
        print("koniec programu nie ma takiej kolejnej liczby w ciagu a")
        break