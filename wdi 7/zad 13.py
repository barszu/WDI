class Node :
    def __init__ (self, val:int , next=None):     #obiekt wskazuje na none(obiekt)
        self.next = next
        self.val = val

    def __str__(self):
        return str(self.val)

def print_all(p):
    if p is not None:
        print(p.val)
        print_all(p.next)

def fn(p): #usuwa od tylu
    if p.next is None: return
    fn(p.next)
    if p.val > p.next.val:
        p.next = p.next.next