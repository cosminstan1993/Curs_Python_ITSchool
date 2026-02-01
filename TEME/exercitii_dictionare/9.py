# 9) Verifica daca o persoana specificata de utilizator exista in dictionar.

dict = {'Daniel' : 26, 
        'Radu' : 19, 
        'Matei' : 17,
          'Eugen' : 34,
            'Maria' : 24
        }

persoana_cautata = input('Cauta o persoana: ').strip().title()
if persoana_cautata in dict: 
    print('persoana pe care o cauti se afla aici')
else:
    print('persoana pe care o cauti nu se afla aici')    