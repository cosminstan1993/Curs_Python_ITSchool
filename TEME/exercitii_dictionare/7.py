# 7) Afiseaza toate persoanele cu varsta peste o valoare specificata de utilizator.

dict = {'Daniel' : 26, 
        'Radu' : 19, 
        'Matei' : 17,
          'Eugen' : 34,
            'Maria' : 24
        }

for nume, varsta in dict.items():
    print(f'{nume} - {varsta}')

valoare = int(input('afisaza persoanele cu varsta peste: '))
print(f"\nPersoanele cu varsta peste {valoare}: ")
for nume, varsta in dict.items():
    if varsta > valoare:
        print(f"{nume} - {varsta}")    