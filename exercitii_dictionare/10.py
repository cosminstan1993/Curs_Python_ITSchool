# 10) Actualizeaza varsta unei persoane specificate de utilizator.

dict = {'Daniel' : 26, 
        'Radu' : 19, 
        'Matei' : 17,
          'Eugen' : 34,
            'Maria' : 24
        }

for nume, varsta in dict.items():
    print(f"{nume} - {varsta}")
print('Modifica varsta unei persoane.')

alegere = input('Introdu numele unei persoane: ').strip().title()

if alegere in dict:
    noua_varsta = int(input(f'introdu noua varsta pentru {alegere}: '))
    dict[alegere] = noua_varsta
    print(f"{alegere} are acum {noua_varsta} ani")
else:
    print('persoana nu se afla pe lista')    
