# 2) Afiseaza varsta unei persoane specifificate de utilizator.

dict = {'Daniel' : 26, 
        'Radu' : 19, 
        'Matei' : 17,
          'Eugen' : 34,
            'Maria' : 24
        }
print('Alege o persoana: ')
for nume in dict.keys():                 #parcurgem cheile dictionarului   
    print(f"- {nume}")
alegere = input('Introdu unmele: ').strip().title()     #facem alegerea titlu si eliminam spatiile 
if nume in dict:
    print(f"{alegere} are {dict[alegere]} ani")
else:
    print('numele ales nu exista')        