# 18) Afiseaza persoanele sortate dupa varsta, de la cea mai mica la cea mai mare. (Utilizati functia sorted pentru a rezolva acest exercitiu).
#    (Folositi functia sorted() si pentru cheia de sortare (key) accesati valorile dictionarului).

dict = {'Daniel' : 26, 
        'Radu' : 19, 
        'Matei' : 17,
          'Eugen' : 34,
            'Maria' : 24
        }

persoane_sortate = sorted(dict.items(), key=lambda items: items[1])

print("persoanele sortate in functie de varste: ")

for nume, varsta in persoane_sortate:
    print(f'{nume} cu varsta de {varsta} ani ')


#sau (dupa chei folosind valoarea ca reper)
print()
print("persoanele sortate in functie de varste: ")

for nume in sorted(dict, key=dict.get):
    print(nume, dict[nume])


#sau (list coprehension)
print()
print("persoanele sortate in functie de varste: ")

persoane_sortate = [(nume, dict[nume]) for nume in sorted(dict, key=dict.get)]
for p in persoane_sortate:
    print(p[0], p[1])