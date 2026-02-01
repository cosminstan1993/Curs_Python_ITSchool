lista = [3, 1, 4, 1, 5, 9, 2]
maxim = lista[0]
minim = lista[0]
for i in lista:
    if i > maxim:
        maxim = i
    if i < minim:
        minim = i
print('maximul este: ', minim)
print('maximul este: ', maxim)            