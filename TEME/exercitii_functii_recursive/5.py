# 5) Scrie o functie recursiva care calculeaza suma tuturor elementelor dintr-o lista imbricata.
# Ex: pentru [1, 2, [3, 4, [5, 6]], 7] returneaza 28

def suma_totala(lista):
    total = 0
    for elem in lista:
        if isinstance(elem, list):
            total += suma_totala(elem)
        else:
            total += elem
    return total


test = [1, 5, 13, [21, 14, [30, 22], [4, 7]]]
print(suma_totala(test))                