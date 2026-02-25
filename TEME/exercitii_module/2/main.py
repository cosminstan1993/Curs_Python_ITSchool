# 2. Sa se creeze un pachet numit "geometry" care sa contina doua module: "area" si 
# "perimeter". Modulul "area" sa contina functii pentru calcularea ariei unui cerc, 
# patrat si dreptunghi, iar modulul "perimeter" sa contina functii pentru calcularea 
# perimetrului acelorasi forme geometrice.
#    Din fisierul principal, sa se importe pachetul si sa se execute fiecare functie
#  cu valori generate aleatoriu.


import random 
from geometry import area, perimeter

r = random.randint(1, 10)
l = random.randint(1, 10)
L = random.randint(1, 10)

print("Valori generate: ")
print("-Raza cerc: ", r)
print('-Latura patrat: ', l)
print("-Lungime dreptunghi: ", L, "-Latime dreptunghi: ", l)


print("\n--- ARII---")
print("-> Arie cerc: ", area.cerc(r))
print("-> Arie patrat: ", area.patrat(l))
print('-> Arie dreptunghi: ', area.dreptunghi(L, l))

print("\n---Perimetre---")
print('-> Perimetru cerc: ', perimeter.cerc(r))
print('-> Perimetru patrat: ', perimeter.patrat(l))
print('-> Perimetru dreptunghi: ', perimeter.dreptunghi(L, l))