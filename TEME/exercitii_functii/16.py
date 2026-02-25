# 16) Scrie o functie care primeste o lista de numere si returneaza o lista doar cu numerele prime.

def numere_prime(lista):
    rezultat = []
    for n in lista:
        if n % 2 == 0:
            rezultat.append(n)
    return rezultat
    

lista_random = []
n = int(input('cate numere vrei sa ai in lista?: '))

for i in range(n):
    numar = int(input('introdu un numar: '))
    lista_random.append(numar)

print("numerele prime din lista ta sunt: ", numere_prime(lista_random))    
