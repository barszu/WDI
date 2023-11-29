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

def contains(h1,h2): #h2 in h1?
    while h2.next is not None: #sprawdzam el z listy 2 czy sa wszytskie w 1
        czy_jest = False
        while h1.next is not None: #lece po 1 liscie
            if h1.val == h2.val :
                czy_jest = True
                break
            h1 = h1.next
        if not czy_jest: return False
        h2 = h2.next
    return True

h1 = Node(None).generate([1,2,3,4,5,6,7,8,9,10])
h2 = Node(None).generate([2,3,5,6,7,8,10,11])
print(contains(h1,h2))