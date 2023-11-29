class Node :
    def __init__ (self, val:int , next=None):     #obiekt wskazuje na none(obiekt)
        self.next = next
        self.val = val

    def __str__(self):
        return str(self.val)
    
    def generate(self,T): #self jako start doklejania
        a = self
        for new_val in T:
            new_obj = Node(new_val)
            a.next = new_obj
            a = a.next
        return self
    
    def print_all(self,p=None):
        if p is not None : a=p
        else: a=self
        while True:
            print(a.val , end="->")
            a = a.next
            if a is None: 
                print("\n")
                return

# c + ax + bx^2 + cx^3
def odejmo_wielomian(h1,h2):
    H = Node(None)
    a , b = h1.next , h2.next
    c = H
    while a is not None and b is not None: #a-b
        new = Node(a.val - b.val)
        c.next = new
        a,b,c = a.next , b.next , c.next
    if a is None and b is not None: #została lista b
        while b is not None:
            new = Node( -1*b.val)
            c.next = new
            b,c = b.next , c.next
    elif a is not None and b is None: #została lista a
            c.next = b
    return H

h1 = Node(None).generate([1,2,3,4,5,6,7])
h2 = Node(None).generate([2,2,2,2,2,2,2,2,2])
odejmo_wielomian(h1,h2).print_all()
