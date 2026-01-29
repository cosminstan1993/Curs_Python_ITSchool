# 11) Afiseaza numarul total de persoane din dictionar.
dict = {'Daniel' : 26, 
        'Radu' : 19, 
        'Matei' : 17,
          'Eugen' : 34,
            'Maria' : 24
        }

numar_persoane = 0

for persoane in dict:
    numar_persoane += 1
print(f"numarul total de persoane este: {numar_persoane}")    