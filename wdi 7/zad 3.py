class Node :
    def __init__ (self, val:int , next=None):     #obiekt wskazuje na none(obiekt)
        self.next = next
        self.val = val

def merge(p,q):
    if p is None: return q #... one dalej maja swoje laczenia
    if q is None: return p #... one dalej maja swoje laczenia
    
    if p.val <= q.val:
        p.next = merge(p.next , q) #rekurencyjnie szukam jak dalej sie ukladaja
        return p
    else:
        q.next = merge(p, q.next)

def merge_iter(p,q):
    p = p.next if p.val == None else p
    q = q.next if q.val == None else q
    h = Node(None)
    a = h
    while p.next is not None and q.next is not None:
        if p.val >= q.val :
            a.next = p
            p = p.next
        elif p.val < q.val :
            a.next = q
            q = q.next
        a = a.next
    if p.next is None and q.next is not None: # zostaly el z q
        a.next = q
    if p.next is not None and q.next is None: #zostaly el z p
        a.next = p
    return h