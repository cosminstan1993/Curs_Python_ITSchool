# 4) Scrie o functie recursiva care calculeaza adancimea(cate liste nivele de liste sunt) unei liste imbricate.
# Ex: pentru [1, 2, [3, 4, [5, 6]], 7] returneaza 3

def adancime(lista):
    max_adancime = 0
    for element in lista:
        if isinstance(element, list):
            max_adancime = max(max_adancime, adancime(element))

    return 1 + max_adancime

l = [1, 2, 3, [4, 7], [22, 40, [21, 40]]]            
print(adancime(l))  