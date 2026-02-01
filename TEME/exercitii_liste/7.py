# Elimină toate elementele pare dintr-o listă de numere.
# Exemplu: [1,2,3,4,5,6] -> [1,3,5]


lista = [1, 2, 3, 4, 5, 6, 7]
rezultat = [x for x in lista if x % 2 !=0]
print(rezultat)