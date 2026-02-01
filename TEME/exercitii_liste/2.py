# 2) Creează o listă cu 7 numere întregi, apoi afișează suma și media elementelor fara a utiliza functiile sum() si avg().
#  Exemplu: [1,2,3,4,5,6,7] -> suma=28, media=4.0
a = int(input('introdu un numar: '))
b = int(input('introdu un numar: '))
c = int(input('introdu un numar: '))
d = int(input('introdu un numar: '))
e = int(input('introdu un numar: '))
f = int(input('introdu un numar: '))
g = int(input('introdu un numar: '))
lista = [a, b, c, d, e, f, g]
suma = 0
for x in lista: 
    suma += x
media = suma / len(lista) 
print('suma =', suma)
print('media =', media)   