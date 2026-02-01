# Interclasează două liste de aceeași lungime într-o singură listă.
# # Exemplu: [1,2], [3,4] => [1,3,2,4]

lista_z = [1, 2]
lista_x = [3, 4]
lista_interclasata = [x for pair in zip(lista_x, lista_z) for x in pair ]
print(lista_interclasata)