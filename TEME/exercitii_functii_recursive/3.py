# 3) Scrie o functie recursiva care calculeaza cate cifre are un numar dat.
# Ex: pentru 1234 returneaza 4

def total_cifre(n):
    if n < 0:
       n = - n
    return n + total_cifre(n // 10) 

n = int(input('introdu un numar: '))
print('Numarul tau are ', total_cifre(n), "cifre")