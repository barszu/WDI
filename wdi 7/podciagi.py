#wdi zad 3 z kolosa 2A 2019/2020
#z ll usun tylko jeden podciag najdluzszy staly
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

def remove_longest(ob):
    #guardian
    head = Node(None,ob)
    
    len_longest = 1
    start_longest = None
    stop_longest = None
    
    start = head
    curr_len = 0
    
    prev = head
    curr = ob
    
    while curr is not None:
        if curr.val == start.next.val :
            curr_len += 1
        else:
            if curr_len > len_longest:
                len_longest = curr_len
                start_longest = start
                stop_longest = curr
            elif curr_len == len_longest:
                len_longest = 1
                start_longest = None
                stop_longest = None
            curr_len = 1
            start = prev
        prev = curr
        curr = curr.next
    
    if curr_len > len_longest:
        len_longest = curr_len
        start_longest = start
        stop_longest = curr
    elif curr_len == len_longest:
        len_longest = 1
        start_longest = None
        stop_longest = None
    
    if len_longest>1: #wywalenie
        start_longest.next = stop_longest
        if start_longest == prev:
            if stop_longest is not None:
                ob.val=stop_longest.val
                ob.next = stop_longest.next
            else: 
                ob.val=None
                ob.next=None
        return len_longest
    return 0