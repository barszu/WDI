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

#1 rosnaca ,  2 losowa , usun z obu powtarzajace sie el
def fn(p1,q1): # p - posortowana
    if p1.val != None:
        h1 = Node(None)
        h1.next = p1
        p1 = h1
    if q1.val != None:
        h2 = Node(None)
        h2.next = q1
        q1 = h2
    
    p , q = p1 , q1
    cnt = 0
    while q is not None and q.next is not None :
        p = p1
        brak_skoku = False
        while p is not None and p.next is not None :
            if p.next.val == q.next.val:
                p.next , q.next = p.next.next , q.next.next
                cnt += 1
                brak_skoku = True
                break
            elif p.next.val > q.next.val : break
            p = p.next
        
        q = q.next if not brak_skoku else q
    return cnt

h1=Node(None).generate([1,2,3,4,5,6,9,10,21,55])
h2=Node(None).generate([90,1,2,3,4,5,6,9,10])
print(fn(h1,h2))
h1.print_all()
h2.print_all()
