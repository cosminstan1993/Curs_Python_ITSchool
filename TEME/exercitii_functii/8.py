# 7) Scrie o funcție care primește o listă de stringuri și returnează o listă cu lungimile fiecărui string.

def lungimi_stringuri(lista):
    lista_lungimi = []
    for string in lista:
        lista_lungimi.append(len(string))
    return lista_lungimi    


lista_stringuri = []
n = int(input('cate propozitii vrei sa scrii?: '))

for _ in range(n):
    text = input('scrie o propozitie: ')
    lista_stringuri.append(text)

print("lungimea fiecarei propozitii: ", lungimi_stringuri(lista_stringuri))    