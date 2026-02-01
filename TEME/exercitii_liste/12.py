# Primește o listă de numere și elimină toate elementele care apar de mai mult de o dată (păstrează doar elementele unice).
# Fara a folosi set().
# # Exemplu: [1,2,2,3,4,4,5] -> [1,3,5]

lista = [ 1, 2, 3, 4, 5, 6, 7, 7, 7, 'matei']
rezultat =[x for x in lista if lista.count(x) == 1]
print(rezultat)


#folosind comanda set():

lista = [ 1, 2, 3, 4, 5, 6, 7, 7, 7, 'matei']
set_unic = set(lista)
print(set_unic)
