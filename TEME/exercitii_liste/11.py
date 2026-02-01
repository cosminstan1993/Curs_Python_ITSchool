# Creează o listă de liste [index, valoare] pentru fiecare element dintr-o listă dată.
# # Exemplu: [10,20,30] -> [[0,10],[1,20],[2,30]]

lista = [10, 20, 30]
rezultat = [[i, v] for i,v in enumerate(lista)]
print(rezultat)