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

def zapis_5(num): #->str
    w = ""
    while num != 0:
        w += str(num%5)
        num = num//5
    return w

def check(num): #True to przenosi
    #czy ma parzysta liczbe "5" w zapisie osemkowym
    w = zapis_5(num)
    return (w.count("5")%2 == 0)


def fn(h):
    a = h.next #bierzacy el,korzystam z nastepnego i na niego patrze
    while True:
        if check(a.next.val): #przenosze nastepny na poczatek
            new = a.next
            a.next = a.next.next #wywalony
            h.next , new.next = new , h.next
        
        a = a.next
        if a is None: return

h = Node(None)
h.generate([10,15,20,30,40,50])
fn(h)
h.print_all()