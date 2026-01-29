# Verifică dacă o listă este palindrom (se citește la fel de la stânga la dreapta și invers).
# # Exemplu: [1,2,3,2,1] -> True, [1,2,3,4] -> False


lista = [2, 3, 4, 5, 7, 5, 4, 3, 'matei']
print(lista == lista[::-1])