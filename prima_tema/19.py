# 19. Primește un număr și afișează tabla înmulțirii pentru acel număr (de la 1 la 10).   

n = int(input('introdu un numar: '))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)