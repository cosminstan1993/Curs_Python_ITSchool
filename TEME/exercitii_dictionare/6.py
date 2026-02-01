# 6) Sterge o persoana specificata de utilizator din dictionar.

dict = {'Daniel' : 26, 
        'Radu' : 19, 
        'Matei' : 17,
          'Eugen' : 34,
            'Maria' : 24
        }

print('Persoane disponibile: ')
for nume in dict:
    print(f"{nume}")
alegere = input('elimina o persoana: ').strip().title()
if alegere in dict:
    dict.pop(alegere)
else:
    print('persoana nu se afla pe lista') 
print('\nDictionarul actualizat: ')
print(dict)           