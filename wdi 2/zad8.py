num = int(input('>>> '))

a = 1
b = 1

x = 1
y = 1

sum_to_num = 0
while sum_to_num < num :
    a , b = b , a+b
    sum_to_num += a
while sum_to_num > num :
    x , y = y , x+y
    sum_to_num -= x
if sum_to_num == num : 
    print("podana liczba jest suma podciagu ciagu fib ->  " + str(num))
else:
    sum_to_num += x
    print("lekko wieksza liczba od podanej jest suma podciagu ciagu fib ->  " + str(sum_to_num))
