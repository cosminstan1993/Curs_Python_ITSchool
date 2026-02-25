# 3) Scrie o funcție care primește două numere și returnează suma, diferența și produsul lor (returnează un tuple).

def operatii(a, b):
    return a + b, a - b, a * b

numarul1 = int(input('introdu primul numar: '))
numarul2 = int(input('introdu al doilea numar: '))   

print(operatii(numarul1, numarul2))


#sau 


def operatii(a, b):
    return a + b, a - b, a * b

numarul1 = int(input('introdu primul numar: '))
numarul2 = int(input('introdu al doilea numar: '))

suma, diferenta, produs = operatii(numarul1, numarul2)

print('Operatii cu numerele alese:')

print(f'- suma numerelor este: {suma}')
print(f'- diferenta numerelor este: {diferenta}')
print(f'- produsul numerelor este: {produs}')