# 1) Sa se afiseze toate puterile lui 2 aflate intre un interval dat de utilizator.
# Exemplu: 10, 50 -> 16, 32

a = int(input('introdu limita inferioara: '))   #am introdus capetele intervalului transformandu-le in numere intregi 
b = int(input('introdu limita superioara: '))
puteri = []    #am creat lista unde stocam toate puterile lui 2 aflate in interval                  
p = 1          #pornim de la cea mai mica putere (1 = 2^0)
while p <= b:  # bucla se opreste cand depaseste limita superioara 
    if p >= a:
        puteri.append(p)  #daca puterea este intre a si b este adaugata in lista 
    p *= 2  # p = p * 2               
print('puterile lui 2 din interval sunt: ', puteri)         