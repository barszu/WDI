class Node :
    def __init__ (self, val:int , next=None):     #obiekt wskazuje na none(obiekt)
        self.next = next
        self.val = val

    def __str__(self):
        return str(self.val)
    
def f(dhead,whead1,whead2): 
    #start ll inputowanej(danej) , poczatek 1st (parzysta dodatnia), poczatek 2nd(nieparzysta ujemna)
    p1 = whead1
    p2 = whead2
    i = dhead.next
    count = 0
    while i is not None:
        
        if i.val %2 == 0 and i.val >0:
            #dodaje do ll1
            p1.next = i
            p1 = p1.next
        elif i.val%2==1 and i.val <0:
            # dodaje do ll2
            p2.next = i
            p2 = p2.next
        else:
            #niby ze usuwam
            count += 1
            temp = i
            i = i.next
            temp.next = None
        
        i = i.next
    p1.next = None
    p2.next = None

def fn_bit(p,a,b):
    cnt = 0
    p = Node(None,p) #dorabiamy wartownika
    
    while p.next is not None:
        q = p.next
        p.next = p.next.next
        
        if q.val % 2 == 0 and q.val > 0 :
            q.next = a.next
            a.next = q
        elif q.val % 2 == 1 and q.val < 0:
            q.next = b.next
            b.next = q
        else:
            cnt += 1
    
    return cnt
    