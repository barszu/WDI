#iterujemy po liscie nie sortowanej i dolatujemy do >= el z sortowanej(optymalizacja)
# jezeli el wystepuje w liscie A to go usuwamy z listy B
# sortujemy liste b
#kleimy
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

def fn(p1,q1):
    from math import inf
    if p1.val != None:
        h1 = Node(-inf)
        h1.next = p1
        p1 = h1
    if q1.val != None:
        h2 = Node(-inf)
        h2.next = q1
        q1 = h2
    
    q = q1
    while q is not None and q.next is not None : #dla el z p1 sprawdzam p2
        p = p1
        brak_iter_q = False
        while p is not None and p.next is not None :
            # kiedy wystapi ten el koniec nic nie robie
            if q.next.val == p.next.val:
                # wywal z listy q q.next
                brak_iter_q = True
                q.next = q.next.next
                break
            elif  ( p.val < q.next.val < p.next.val ): #wstaw q.next pomiedzy i odepnij
                temp = q.next
                q.next = q.next.next
                p.next , temp.next = temp , p.next
                brak_iter_q = True
                break
            else:
                p = p.next
            
        
        if not brak_iter_q: q = q.next
    return p1

p=Node(None).generate([1,5,8,90,130])
q=Node(None).generate([2,5,8,50,130,2137])
fn(p.next,q.next).print_all()
