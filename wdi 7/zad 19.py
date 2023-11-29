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

def uniq(h):
    a = h #wolny wskaznik chodzacy iteracyjnie na nowej liscie 
    # b = h #w iteracjach chodzi
    c = 0
    while a.next is not None:
        b_old = a
        b = a.next
        v = a.val
        while b is not None:
            if b.val == v:
                b_old.next = b.next
                b = b.next
                c += 1
            else: b , b_old = b.next , b_old.next
        
        a = a.next
    print(c)

h = Node(None)
h.generate([25,55,2,2,2,5,8,10])
uniq(h)
h.print_all()