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

def iloczyn(p,q):
    # p (lista 1st)
    # q (lista 2nd)
    # x (lista wynikowa)
    if p is None or q is None: return None
    if p.val == q.val:
        x = p
        p , q = p.next , q.next
        x.next = iloczyn(p , q) #patrze co dalej
        return x
    else:
        if p.val < q.val:
            return iloczyn(p.next,q)
        else:
            return iloczyn(p,q.next)

def iloczyn_3(z1,z2,z3):
    return iloczyn(z1 , iloczyn(z2,z3))

p = Node(None).generate([2,3,5])
q = Node(None).generate([1,2,4])
iloczyn(p,q).print_all()

