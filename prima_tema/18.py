# 18. Primește un text și afișează fiecare cuvânt pe o linie nouă.

text = input('scrie un text si eu ti-l scot pe cuvinte: ')

cuvinte = text.split()

rezultat = "\n".join(cuvant for cuvant in cuvinte)
print(rezultat)