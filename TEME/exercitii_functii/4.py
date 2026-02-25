# 4) Scrie o funcție care primește un număr și returnează True dacă este par, altfel False.

def par_impar(a):
    if a % 2 == 0:
        return True
    else:
        return False

numar = int(input('alege un numar iar eu iti zic daca e par: '))

print(par_impar(numar))