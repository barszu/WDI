#n - liczba cyfr
n = 3

a = int("1" + ("0"*(n-1)))
b = int("9"*n)
for num in range(a , b+1 ):
    ciag = 0
    for cyfra in str(num):
        ciag += int(cyfra)**n
    if ciag == num :
        print(num)