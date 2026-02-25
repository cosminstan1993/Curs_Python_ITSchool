# 1. Sa se creeze un modul numit "operations" care sa contina functii pentru adunare,
#  scadere, inmultire si impartire a doua numere.
#    Din fisierul principal, sa se importe modulul si sa se execute fiecare operatie cu 
# doua numere generate aleatoriu.

import operations
import random

a = random.randint(1, 10)
b = random.randint(1, 10)

print('Numerele sunt: ', a, "si", b)

print('Adunare: ', operations.adunare(a, b))
print('Scadere: ', operations.scadere(a, b))
print('Inmultire: ', operations.inmultire(a, b))
print('Impartire: ', operations.impartire(a, b))