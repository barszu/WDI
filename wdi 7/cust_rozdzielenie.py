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

#funkcja z duzej listy robi liste A i B
#w liscie A sa el. co powtarzaja sie dokladnie 2 razy
#w liscie B reszta

def two(head):
    H2 = Node(None)
    r = H2
    
    p = Node(None)
    p.next = head
    head = p
    #uzywamy nexta
    while p.next is not None:
        curr_val = p.next.val
        curr__val_count = 0
        q = head
        while q.next is not None:
            if q.next.val == curr_val:
                curr__val_count += 1
            q = q.next
        if curr__val_count == 2:
            q = p 
            while q.next is not None:
                if q.next.val == curr_val:
                    r.next = q.next
                    r = r.next
                    q.next = q.next.next
                    return None
                else:
                    q = q.next
        else:
            p = p.next
    return H2.next , head.next