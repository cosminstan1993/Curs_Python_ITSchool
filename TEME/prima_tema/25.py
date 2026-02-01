# 25. Primește un text și afișează doar caracterele care sunt cifre.

text = input('scrie un text barosane: ')
rezultat = ' '.join(cifre for cifre in text if cifre.isdigit())
print('cifrele din textul tau: ', rezultat)