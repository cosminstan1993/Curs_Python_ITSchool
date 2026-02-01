# 24. Primește un număr și afișează suma cifrelor sale.

n = input('introdu un numar: ')
suma = 0 
for cifra in n:
    suma += int(cifra)  
    
print(suma)