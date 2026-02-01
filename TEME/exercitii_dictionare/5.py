# 5) Afiseaza varsta medie a persoanelor din dictionar.

dict = {'Daniel' : 26, 
        'Radu' : 19, 
        'Matei' : 17,
          'Eugen' : 34,
            'Maria' : 24
        }

varste = dict.values()
media_varstelor = sum(varste) / len(dict)
print(media_varstelor)

#sau

media = sum(dict.values()) / len(dict)
print(media)