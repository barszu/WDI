class Node:
    def __init__(self,a,n,next=None) : #a x^n
        self.a = a
        self.n = n
        self.next = next

def print_all(p):
    first = True
    while p is not None:
        if not first:
            print(" + ", end = "")
        
        print(str(p.a) + "x^" + str(p.n), end = "" )
        first = False
        p = p.next

def create_from_list(L):
    g = Node(None,None)
    current = g
    
    for a , n in L :
        current.next = Node(a,n)
        current = current.next
    
    return g.next

def substract(x,y): #rekurencyjna
    if y is None: return x
    if x is None:
        y.val *= (-1)
        y.next = substract(x,y.next)
        return y
    
    if x.n == x.n:
        x.a -= y.a
        x.next = substract(x.next,y.next)
        return x
    else:
        if x.n < y.n : 
            x.next = substract(x.next,y)
            return x
        else:
            y.next = substract(x,y.next)
            return y

p = create_from_list([[1,1],[2,2],[1,3]])
q = create_from_list([[3,1],[1,2],[4,4]])
a = substract(p,q)
print_all(a)