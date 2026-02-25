# Sa se scrie un program care citeste de la tastatura informatii desre persone (nume, prenume, varsta, oras)
# pana la introducerea cuvantului "exit" si le salveaza intr-un fisier JSON numit "persoana.json".


import json
import os

file_path = "TEME/exercitii_JSON_CSV/1/persoana.json"

if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        persoane =json.load(file)

else:
    persoane = []

while True:
   print("\n1 - Adauga persoana")
   print("2 - Sterge persoana dupa nume")
   print("3 - Afisaza persoane")
   print("4 - Exit")
   
   optiune = input("Alege optiunea: ")
    
   if optiune == "1":
       nume = input("Nume: ")
       prenume = input("Prenume: ")
       varsta = input("Varsta: ")
       oras = input("Oras: ")
       
       persoana ={
        "nume": nume,
        "prenume": prenume,
        "varsta": varsta,
        "oras": oras
     }
    
       persoane.append(persoana)
       print("Persoana adaugata.")

   elif optiune == "2":
     nume_sters = input("Introdu numele persoanei de sters: ")
       
     persoane_noi = []
     
     for persoana in persoane:
         if persoana["nume"] != nume_sters:
             persoane_noi.append(persoana)
             
     persoane = persoane_noi
     print("Persoana a fost stearsa (daca exista)")       
     
   elif optiune == "3":
        for persoana in persoane:
            print(persoana) 
            
   elif optiune == "4":
        break
    
   else:
        print("optiune invalida.")
            
    
with open("TEME/exercitii_JSON_CSV/1/persoana.json", "w", encoding="utf-8") as file:
    json.dump(persoane, file, indent=4, ensure_ascii=False)

print("Datele au fost salvate in persoana.json")    


#Am facut programul ca sa si pot sterge persoane dupa nume.