# 4) Afișează toate elementele de pe poziții impare dintr-o listă dată.
# Exemplu: [10,20,30,40,50,60] -> 20,40,60

lista = list(input('introdu elemente in lista: ').split())
for i in range(len(lista)):
    if i % 2 == 1:
      print(lista[i], end=" ")