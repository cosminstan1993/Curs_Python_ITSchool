# 3) Afiseaza cea mai mare si cea mai mica varsta din dictionar.

dict = {'Daniel' : 26, 
        'Radu' : 19, 
        'Matei' : 17,
          'Eugen' : 34,
            'Maria' : 24
        }

min_varsta = min(dict, key=dict.get) 
max_varsta = max(dict, key=dict.get)

print(f"cea mai mica persoana: {min_varsta} ({dict[min_varsta]})")
print(f'cea mai mare persoana: {max_varsta} ({dict[max_varsta]})')