# 2. Sa se scrie un program care citeste un fisier text numit "date.txt" si afiseaza numarul de linii, cuvinte si caractere din 
# fisier.

with open("TEME/exercitii_fisiere/2/date.txt", "r", encoding="utf-8") as f:
    linii = f.readlines()

numar_linii = len(linii) 
numar_cuvinte = sum(len(linie.split()) for linie in linii)
numar_caractere = sum(len(linie) for linie in linii)

print("-> Numarul de linii: ", numar_linii)
print('-> Numarul de cuvinte: ', numar_cuvinte)
print("-> Numarul de caractere: ", numar_caractere)