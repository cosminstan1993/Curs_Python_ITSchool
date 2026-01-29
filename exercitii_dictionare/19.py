# 19) Se da urmatorul text: "Ana are 12 ani, Ion are 15 ani, Maria are 12 ani, George are 15 ani, Elena are 14 ani".
#     Creeaza un dictionar care sa contina numele persoanelor ca si chei si varstele ca si valori.


text = "Ana are 12 ani, Ion are 15 ani, Maria are 12 ani, George are 15 ani, Elena are 14 ani"

persoane = {}
propozitii = text.split(", ")

for parti in propozitii:
    cuvinte = parti.split(" ")
    nume = cuvinte[0]
    varsta = int(cuvinte[2])
    persoane[nume] = varsta 

print(persoane)
