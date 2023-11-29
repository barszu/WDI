a = 1
b = 7
import sys

result = ""
tablica_reszt = [None]*b
reszta = a%b
# lista = [id 0 , id1 , id2, id3 , id4 ,id5 , id6 , id7] id odpopwiada jaka reszta byla 
# a to co zostaje wpisane to na jakiej pozycji bylo a ta reszta
#kiedy reszta sie powtorzy to znaczy ze jest koniec okresu
while (reszta != 0 and tablica_reszt[reszta] == None):
    tablica_reszt[reszta] = len(result)
    reszta = reszta*10
    iloraz = reszta // b
    result += str(iloraz)
    reszta = reszta % b
if reszta == 0 :
    print(a/b)
    sys.exit()
else:
    print(str((a//b)) + "." + str(result[:tablica_reszt[reszta]]) + "(" + str(result[tablica_reszt[reszta]:]) + ")")
    sys.exit()
