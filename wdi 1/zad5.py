# def mod(x):
#     if x < 0 :
#         return (x * -1)
#     else:
#         return x

sqrt_num = (21)
precision = 0.000000001
a = 1
b = sqrt_num
while abs(a - b) > precision :
    a  , b = (a + b)/2 , sqrt_num/a
print(a)