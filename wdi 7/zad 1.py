class Node :
    def __init__ (self, val:int , next=None):     #obiekt wskazuje na none(obiekt)
        self.next = next
        self.val = val

#GUARDIAN to head tej listy jako None lepiej zaczynac ta liste w ten sposob

#zakladam ze ten set to link lista odrazu posortowana
def add(obiekt_startowy , wartosc_do_wstawienia): #pracuje na elemencie kolejnym | funkcja void

    if obiekt_startowy.next is None: # obiekt startowy pokazuje na cos | czy to jest to samo co obiekt none
        #jestem na koncu listy wiec musze dokleic obiekt
        new_obj = Node(wartosc_do_wstawienia) # pokazuje on odrazu na None
        obiekt_startowy.next = new_obj
        return
    if obiekt_startowy.val == None : return add(obiekt_startowy.next , wartosc_do_wstawienia)
    if obiekt_startowy.val < wartosc_do_wstawienia and (obiekt_startowy.next).val > wartosc_do_wstawienia:
        #wstaw
        new_obj = Node(wartosc_do_wstawienia)
        new_obj.next = obiekt_startowy.next
        obiekt_startowy.next = new_obj
        return
    if obiekt_startowy.val < wartosc_do_wstawienia and (obiekt_startowy.next).val < wartosc_do_wstawienia:
        return add(obiekt_startowy.next , wartosc_do_wstawienia) #dalsza iteracja po link liscie
    if obiekt_startowy.val == wartosc_do_wstawienia:
        #ta wartosc juz jest nie mozna wstawic tego
        return

def is_present(ob , val): #czy val znajduje sie w liscie
    
    if ob.next is None : return False # nie ma tego el w liscie dotarlismy do konca
    if ob.val == None: return is_present(ob.next , val)
    if ob.val == val: return True
    if val < ob.val: return False
    return is_present(ob.next , val)

# def delete(ob , value): #void
#     if ob.next is None : return
#     if ob.val == None: return delete(ob.next , value) #zastrzerzenie beldow przy porownywaniu
#     if ob.val > value : return #dalej go nie ma
#     if (ob.next).val == value :
#         ob.next = (ob.next).next 
#     return delete(ob.next , value)

def delete_2_(g , val): #patrz na kolejne a nie na bierzacy
    if g.next is None: return
    if g.next.val == val: g.next = g.next.next
    elif g.next.val < val:
        delete_2_(g.next, val)

z = Node(15)
y = Node(10 , z)
x = Node(5,y)
g = Node(None,x) #guardian

p = Node(1)
gp = Node(None , p)

def print_obj(g):
    a = g.next
    while a is not None:
        print(a.val)
        a = a.next
    return

print_obj(gp)
delete_2_(gp,1)
print_obj(gp)

# print_obj(g)
# print("add")
# add(g,7)
# print_obj(g)
# print(is_present(g,7))
# print(is_present(g,8))
# delete(g,7)
# print_obj(g)
