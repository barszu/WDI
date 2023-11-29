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

#ll zawiera przedzialy przefiltruj je/ merguj
def how_merge(a1,a2,b1,b2): #-> 
    # 0 (nie ma nic wspolnego)
    # 1 (czesciowe <a1,b2>)
    # 2 (calkowite <a1,b1> )
    # if a1 > a2: 
    #     a1 , b1 , a2 , b2 = a2 , b2 , a1 , b1
    if a2>b1 : return 0
    if a1 <= a2 <= b1 :
        if a1 <= b2 <= b1: return 2
        else: return 1

def filter(h):
    a = h.next
    while a is not None: #iterator zwyklych ktore beda edytowane
        b = h.next
        b_old = h
        while b is not None: #iterator tych co moga byc usuniete
            if b is a : 
                b , b_old = b.next , b
                continue
            a1 , b1 = a.val [0] , a.val [1]
            a2 , b2 = b.val [0] , b.val [1]
            if a1 > a2: a1 , b1 , a2 , b2 = a2 , b2 , a1 , b1
            h_merge = how_merge(a1,a2,b1,b2)
            if h_merge == 0: #nie ma czesci wspolnej, nic nie usunalem
                b , b_old = b.next , b
            elif h_merge == 1: #czesciowo lacza usunac el b i dalsza iteracja
                a.val = (a1,b2)
                #usun el b
                b_old.next = b.next
                b = b_old.next
            elif h_merge == 2: #calkowicie sie laczy usun b
                a.val = (a1,b1)
                #usun el b
                b_old.next = b.next
                b = b_old.next
        
        a = a.next

h = Node(None)
h.generate([(2,5),(3,8)]) #values as tuples
h.print_all()
filter(h)
h.print_all()

