# 14) Creeaza o lista care contine toate varstele din dictionar, fara duplicate, si afiseaz-o.

dict = {'Daniel' : 26, 
        'Radu' : 19, 
        'Matei' : 17,
          'Eugen' : 34,
            'Maria' : 24
        }


lista_varste = sorted(set(dict.values()))
print(lista_varste)
