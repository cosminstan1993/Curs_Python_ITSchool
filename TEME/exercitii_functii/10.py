# 10) Scrie o functie care primeste un dictionar de forma {nume: varsta} si returneaza numele persoanei cu cea mai mica varsta.

def min_varsta(dictionar):
    nume_min = None
    varsta_min = None
    for nume, varsta in dictionar.items():
        if varsta_min is None or varsta < varsta_min:
            varsta_min = varsta
            nume_min = nume
    return nume_min


persoane = {}
n = int(input('cate persoane vrei sa introduci?: '))

for i in range(n):
    nume = input('introdu numele persoanei: ')
    varsta = int(input(f'introdu varsta lui {nume}: '))
    persoane[nume] = varsta

print('persoana cu cea mai mica varsta este: ', min_varsta(persoane))    