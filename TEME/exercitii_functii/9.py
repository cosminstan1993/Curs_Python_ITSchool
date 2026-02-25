# 9) Scrie o funcție care primește doua liste de numere si returneaza o lista cu numerele comune celor doua liste.

def numere_comune(a, b):
    lista_comuna = []
    for x in a:
        if x in b and x not in lista_comuna:
            lista_comuna.append(x)
    return lista_comuna        

first_list = []
n = int(input('cate numere vrei sa ai in prima lista?: '))
for i in range(n):
    numar = int(input('introdu un numar: '))
    first_list.append(numar)


second_list = []
n = int(input('cate numere vrei sa ai in a doua lista?: '))
for i in range(n):
    numar = int(input("introdu un numar: "))
    second_list.append(numar)

print('numerele comune din listele tale: ', numere_comune(first_list, second_list))