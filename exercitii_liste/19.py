#  Scrieti un program care sa genereze un numar aleator intre 1 si 100. Utilizatorul trebuie sa
# ghiceasca numarul, iar programul sa ii ofere indicatii daca numarul introdus este mai mare sau mai mic decat cel generat.
# Programul se termina cand utilizatorul ghiceste numarul corect sau daca introduce cuvantul exit. La final se afiseaza numarul de incercari facute.

# Pentru generarea numarului aleator:
# import random
# numar_aleator = random.randint(1, 100)


import random
numalr_ales = random.randint(1, 100)

nr_ghicit = ''
count = 1 
flag = True

while flag:
    nr_ghicit = int(input('ghiceste numarul: '))
    if numalr_ales == nr_ghicit:
        print('ai ghicit numarul')
        