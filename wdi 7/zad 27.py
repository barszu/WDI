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

def merge_rek2(p,q):
    p = p.next if p.val == None else p
    q = q.next if q.val == None else q
    # global H
    H = Node(None)
    
    def recursion(p,q,h):
        if p is None: 
            h.next = q
            return  #... one dalej maja swoje laczenia
        if q is None: 
            h.next = p
            return #... one dalej maja swoje laczenia
        
        if p.val <= q.val:
            h.next = p
            recursion(p.next,q,h.next)
        else:
            h.next = q
            recursion(p, q.next, h.next)
        # H.print_all()
    
    recursion(p,q,H)
    return H

def merge_iter(p,q):
    p = p.next if p.val == None else p
    q = q.next if q.val == None else q
    H = Node(None)
    start = H
    while p.next is not None and q.next is not None:
        if p.val <= q.val: #wklej p
            H.next , p = p , p.next
            H = H.next
        else: #wklej q
            H.next , q = q , q.next
            H = H.next
    
    if p.next is None:
        H.next = q
    elif q.next is None:
        H.next = p
    return start







h1 = Node(None)
h2 = Node(None)
h1.generate([4,5,6])
h2.generate([4,8,90])
hr = merge_iter(h1,h2)
hr.print_all()