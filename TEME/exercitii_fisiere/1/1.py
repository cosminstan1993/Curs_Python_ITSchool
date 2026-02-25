# 1. Sa se scrie un program care citeste de la tastatura informatii despre persoane (nume, prenume, varsta, oras)
#    si le salveaza intr-un fisier text numit "persoana.txt" in formatul: "Nume Prenume, Varsta, Oras".

f = open("TEME/exercitii_fisiere/1/persoana.txt", 'a')

while True:
    nume = input("Nume: ")
    prenume = input("Prenume: ")
    varsta = input('Varsta: ')
    oras = input('Oras: ')

    f.write(nume + " " + prenume + ", " + varsta + ", " + oras + "\n")

    raspuns = input("Mai adaugi? (d/n): ")
    if raspuns == "n" :
        break


f.close() 
print("Gata! Datele au fost salvate.")   

