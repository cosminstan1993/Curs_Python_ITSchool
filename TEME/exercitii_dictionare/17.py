# 17) Afiseaza persoanele sortate alfabetic dupa nume. (Utilizati functia sorted pentru a rezolva acest exercitiu).

dict = {'Daniel' : 26, 
        'Radu' : 19, 
        'Matei' : 17,
          'Eugen' : 34,
            'Maria' : 24
        }

for nume in sorted(dict):
    print(f'{nume} - {dict[nume]}')
