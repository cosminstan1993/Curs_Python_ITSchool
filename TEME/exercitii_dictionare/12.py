# 12) Creeaza o lista cu toate numele persoanelor din dictionar si afiseaza-le.

dict = {'Daniel' : 26, 
        'Radu' : 19, 
        'Matei' : 17,
          'Eugen' : 34,
            'Maria' : 24
        }


lista_nume = list(dict.keys())
print(lista_nume)

#cu bucla for 

lista_nume = []
for nume in dict:
    lista_nume.append(nume)
print(lista_nume)

#cu list comprehension

lista_nume = [nume for nume in dict]
print(lista_nume)