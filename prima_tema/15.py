# 15. Primește un număr n și afișează toate numerele pare de la 0 la n (inclusiv).

n = int(input('introdu un numar: '))
rezultat = [p for p in range(0, n+1) if p % 2 == 0]
print('toate numerele pare de la 0 pana la numarul tau: ', rezultat)