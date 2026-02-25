# 2) Scrie o funcție recursivă care calculează suma numerelor de la 1 la n.
# Ex: pentru n=5, returnează 15 (1+2+3+4+5)

def suma(n):
    if n == 1:
        return 1
    return n + suma(n - 1)    

n = int(input('introdu un numar: '))
print(f'Suma numerelor de la 1 pana la {n}: ', suma(n))
