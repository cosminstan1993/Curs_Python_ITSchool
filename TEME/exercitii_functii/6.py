# 6) Scrie o funcție care primește o listă de numere și returnează suma tuturor numerelor.

def suma_lista(lista):
    total = 0
    for numar in lista:
        total += numar
    return total

lista = [5, 6, 9, 12]
print(suma_lista(lista))

#sau 
print("Variant in care introduci tu numerele:")
   

lista = []
n = int(input('Cate numere vrei sa introduci?: '))

for i in range(n):
    numar = int(input('introdu un numar: '))
    lista.append(numar)

print('suma numerelor este: ', suma_lista(lista))

#sau 

char = input('introdu sirul')
numar_clar = char.split('|')
lista = [int(i.strip()) for i in numar_clar]

rezultat = suma_lista(lista)
print(rezultat)