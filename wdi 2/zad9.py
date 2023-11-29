x , dx = 1 , 0.1
def f(x): return (1/x)
k = 100
pole = 0
while x < k :
    x += dx
    pole += dx*f(x)
print(pole)