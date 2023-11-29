def nwd(num1 , num2):
    if num2 > num1:
        num1 , num2 = num2 , num1
    while True:
        modulo = num1%num2
        if modulo == 0 :
            return num2
            break
        else:
            num1 , num2 = num2 , modulo
            
a = 12
b = 15
c = 9

print(nwd((nwd(a,b)),c))
