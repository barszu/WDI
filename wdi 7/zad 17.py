class Node :
    def __init__ (self, val:int , next=None):     #obiekt wskazuje na none(obiekt)
        self.next = next
        self.val = val

    def __str__(self):
        return str(self.val)

#klucz to val
#true to zostaje w liscie
def check_ONES(i): #-> bool
    return bin(i)[2:].count("1") % 2 == 1 

#z guardianem
def fn(head): #guardian
    p = head #nowa lista do ktorej bedzie klejone
    i = head #iterator po starej liscie
    while i.next is not None: #iteracja 
        i = i.next
        if not check_ONES(i.val):
            p.next = i #klejenie do p 
            p = p.next
    p.next=None
    #referencja zadziala i zepsuje zmienne
    return p

class Node_2 :
    def __init__ (self, val:int , next=None , prev=None):     #obiekt wskazuje na none(obiekt)
        self.next = next
        self.val = val
        self.prev = prev

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

def delete(ob):
    p = ob.prev
    q = ob.next
    p.next , q.prev = q , p