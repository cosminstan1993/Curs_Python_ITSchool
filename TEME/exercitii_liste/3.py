# 4) Primește o listă de la tastatură (elemente separate prin spațiu) și afișează lista inversată.
# Exemplu: input: 1 2 3 4 5 -> output: [5,4,3,2,1]

lista = list(map(int, input('introdu elementele separate prin spatiu: ').split()))
lista_inversata = []
for i in range(len(lista) - 1, -1, -1):
    lista_inversata.append(lista[i])
print(lista_inversata)    