# 15) Afiseaza persoana cu cea mai apropiata varsta de o valoare specificata de utilizator.

dict = {'Daniel' : 26, 
        'Radu' : 19, 
        'Matei' : 17,
          'Eugen' : 34,
            'Maria' : 24
        }

alegere = int(input('scrie o varsta: '))

persoana_apropiata = min(dict, key = lambda nume : abs(dict[nume] - alegere))
print(f"persoana cea mai apropiata ca si varsta este {persoana_apropiata} ({dict[persoana_apropiata]} ani)")