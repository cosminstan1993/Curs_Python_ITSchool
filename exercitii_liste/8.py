# Primește o listă de stringuri și construiește o nouă listă cu stringurile care conțin litera 'a'.
# Exemplu: ['ana', 'mere', 'casa', 'masina'] -> ['ana', 'casa', 'masina']

lista = ['adrian', 'matei', 'florian', 'gabriel', 'edi']
rezultat =[x for x in lista if 'a'in x ]
print(rezultat)