# Sa se numere de cate ori apare un element intr-o lista incluzand si listele imbricate.
# # Exemplu: [1, 2, [3, 1, 4], 7, [1, 2, [1, 5]]] si elementul 1 -> apare de 4 ori


lista = [1, 2, [3, 1, 4], 7, [1, 2, [1,5]]]

def count(l):
    total = 0
    for x in l:
        if isinstance(x, list):
            total += count(x)
        elif x == 1:
            total += 1
    return total

rezultat = count(lista)

print('elementul 1 apare de ', rezultat)
            
#sau

lista_elemente = [1, 2, [3, 1, 4], 7, [1, 2, [1, 5]]]
element = 1

count = 0
index = 0
while index < len(lista_elemente):
    if isinstance(lista_elemente[index], list):
        lista_elemente.extend(lista_elemente[index])
    else:
        if lista_elemente[index] == element:
            count += 1

    index += 1

print('elementul 1 apare de ', count)    