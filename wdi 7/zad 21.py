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

#lista wejsciowa ma guardiana
def fn(h):
    #ciagi rosnace najdluzsze
    longest_len = 1
    longest_len_2 = 1
    p , q , i = h ,h ,h
    temp_len = 0
    longest_p , longest_q = h , h
    
    i = i.next
    temp_len += 1
    
    while i.next is not None:
        # i = i.next
        # temp_len += 1
        
        if not i.next.val > i.val: #dziura w rosnacym i ostatnim el
            q = i #p
            if temp_len > longest_len:
                longest_p , longest_q = p , q
                longest_len , longest_len_2 = temp_len , longest_len
                
            elif temp_len > longest_len_2:
                longest_len_2 = temp_len
            #przygotowanie na kolejna iteracje
            p , q = i , i
            temp_len = 0
        
        i = i.next
        temp_len += 1
        
    #po iteracjach
    if temp_len > 1: #zostal sie podciag a lista sie skonczyla
        q = i #p
        if temp_len > longest_len:
            longest_p , longest_q = p , q
            longest_len , longest_len_2 = temp_len , longest_len
            
        elif temp_len > longest_len_2:
            longest_len_2 = temp_len

    if longest_len != longest_len_2 : #usun liste najdluzsza
        longest_p.next = longest_q.next


h = Node(None).generate([1,0,1,9,15,16,17,18,19,20,21,22,1,1,1,6,7,8,9,10,2,0])
h.print_all()
fn(h)
h.print_all()