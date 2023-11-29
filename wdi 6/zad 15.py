#z pozdrowieniami dla szanownego pana prodziekanaa ❤
def factorial(a):
    if a <= 0 : return factorial(abs(a))
    if a == 1 : return 1
    return a*factorial(a-1)

def checkmate(x, y, tab):
    for i in range(8):
        tab[x][i] = 1
        tab[i][y] = 1

    while True:
        lu, ld, ru, rd = 1, 1, 1, 1
        while x - lu >= 0 and y - lu >= 0:
            tab[x - lu] [y - lu] = 1
            lu += 1
        while x + ld < 8 and y - ld >= 0:
            tab[x + ld] [y - ld] = 1
            ld += 1
        while x + rd < 8 and y + rd  < 8:
            tab[x + rd] [y + rd ] = 1
            rd += 1
        while x - ru >= 0 and y + ru  < 8:
            tab[x - ru] [y + ru] = 1
            ru += 1
        break


def hetman(tab, h=0):
    if h == 8:
        return 1
    result = 0
    for k in range(8):
        if tab[h][k] == 0:
            new_tab = [[tab[i][j] for j in range(8)] for i in range(8)]
            checkmate(h, k, new_tab)
            result += hetman(new_tab, h+1)
    return result

t = [ [0]*8 for _ in range(8) ]
print(hetman(t)*factorial(8))