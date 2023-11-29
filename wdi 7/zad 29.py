#zrob zeby 2 ll byly takie same - wywalaj elementy ktore sa
# obie rosnace
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

def same(p1,q1):
    if p1.val != None:
        h1 = Node(None)
        h1.next = p1
        p1 = h1
    if q1.val != None:
        h2 = Node(None)
        h2.next = q1
        q1 = h2
    
    
    
    def fn_pomoc(p1,q1):
        p = p1
        while p is not None and p.next is not None : #dla el z p1 sprawdzam p2
            q = q1
            czy_jest = False
            while q is not None and q.next is not None :
                # kiedy wystapi ten el to nie ma sensu sprawdzac
                if q.next.val == p.next.val:
                    czy_jest = True
                    break
                #tego el juz nie bedzie
                elif q.next.val > p.next.val: break
                else: q = q.next
            
            if not czy_jest: # nie ma tego el w 2 liscie -> wywal go (lista p)
                p.next = p.next.next
            else:
                p = p.next
        return
    fn_pomoc(p1,q1)
    fn_pomoc(q1,p1)
    return (p1,q1)

p1=Node(None).generate([1,2,3,4,5,10,20,30])
q1=Node(None).generate([1,2,3,5,47,90,130])
same(p1,q1)
p1.print_all()
q1.print_all()
