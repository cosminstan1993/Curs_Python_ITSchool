# 8) Afiseaza toate persoanele din dictionar in urmatorul format: "Nume: <nume_persoana>, Varsta: <varsta_persoana>".

dict = {'Daniel' : 26, 
        'Radu' : 19, 
        'Matei' : 17,
          'Eugen' : 34,
            'Maria' : 24
        }


for nume, varsta in dict.items():
    print(f"Numele :{nume} - Varsta :{varsta}")