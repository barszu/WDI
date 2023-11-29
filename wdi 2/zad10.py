num = int(input(">>> "))
a = 2
while num >= a :
    if num%a == 0 :
        print(str(num) + " jest wielokrotnoscia jakiegos wyrazu z ciagu")
        break
    a = 3*a + 1