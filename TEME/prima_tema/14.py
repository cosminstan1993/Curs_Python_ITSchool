# 14. Primește un text și construiește un nou string numai cu vocalele din el.

text = input('scrie ce vrei tu: ')
vocale = 'a, e, i, o, u, A, E, I, O, U'
rezultat = ""
for c in text:
    if c in vocale:
        rezultat += c
print(rezultat)        


#sau

text = input('scrie ce vrei tu: ')
vocale = 'aeiouAEIOU'

rezultat = [c for c in text if c in vocale]
print(rezultat)