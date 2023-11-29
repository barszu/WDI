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
    
    def print_cycle(self): #sypie sie dla cyklu dl 1, 2
        if self.next is self :
            print(self.val , end="->")
            print("...\n")
            return
        elif self.next.next is self:
            print(self.val , end="->")
            print(self.next.val , end="->")
            print("...\n")
            return
        
        a = self
        print(a.val , end="->")
        a = a.next
        while a.next is not self:
            print(a.val , end="->")
            a = a.next
        print(a.val , end="->")
        print("...\n")
        return
    
    def generate_cycle(self,T): #self jako start doklejania
        a = self
        for new_val in T:
            new_obj = Node(new_val)
            a.next = new_obj
            a = a.next
        a.next = self
        return self

def count(start,val):
    c = 0
    a = start
    while a.next is not start:
        if a.val == val : c += 1
        a = a.next
    if a.val == val : c += 1
    return c

def delete(start,val):
    #wstaw
    g = Node(None)
    start.next , g.next = g , start.next
    a = g
    while a.next is not g:
        if a.next.val == val: #usun go
            a.next = a.next.next
        else: a = a.next
    #usuwam guardiana
    a.next = a.next.next
    return a.next

def usun_pow(start,k): #TODO
    a = start
    g = Node(None)
    start.next , g.next = g , start.next
    a = g
    if count(a,a.val) == k :
            a = delete(a,a.val) #bez iteracji po usunieciu
    else:
        a = a.next
    while a.next is not g or a is not g: #TODO #dla ostatniego sie nie wykona
        # dla el a.next szukam ilosc powtorzen
        if count(a,a.val) == k :
            a = delete(a,a.val) #bez iteracji po usunieciu
        else:
            a = a.next
    if count(a,a.val) == k :
        a = delete(a,a.val) #ostatni
    return a.next

def usun_pow(start,k): #TODO
    a = start
    g = Node(None)
    start.next , g.next = g , start.next
    a = g
    while a.next is not g : #TODO #dla ostatniego sie nie wykona
        # dla el a.next szukam ilosc powtorzen
        if count(a,a.val) == k :
            a = delete(a,a.val) #bez iteracji po usunieciu
        else:
            a = a.next
    if count(a,a.val) == k :
        a = delete(a,a.val) #ostatni
    return a.next


# a=Node(1)
# b=Node(2)
# c=Node(2)
# a.next = b
# b.next = c
# c.next = a
# print(count(a,1))
# a.print_cycle()
# delete(a,1).print_cycle()

a=Node(1).generate_cycle([1,2,3,5,11,1,1,1,4])
a.print_cycle()
usun_pow(a,2).print_cycle()

