a = 1
b = 1
in_sum = 21
suma = 2
while suma <= in_sum:
    a , b = b , a+b
    suma += b
    
a = 1
b = 1
    
while True:
    if suma == in_sum:
        print("podciag o sumie {} ".format(in_sum) + '\x1b[38;2;255;0;0m\x1b[48;2;255;255;0m' + "JEST" + '\x1b[0m' + " w ciagu fib" )
        break
    elif suma < in_sum : 
        print("podciag o sumie {} ".format(in_sum) + '\x1b[38;2;255;0;0m\x1b[48;2;255;255;0m' + " NIE JEST" + '\x1b[0m' + " w ciagu fib" )
        break
    suma -= a
    a , b = b , a+b
