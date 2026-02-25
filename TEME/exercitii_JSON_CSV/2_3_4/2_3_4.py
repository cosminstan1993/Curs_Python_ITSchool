# Sa se scrie un program care citeste date despre produse (nume, pret, cantitate) de la tastatura pana la introducerea cuvantului "exit" si le salveaza intr-un fisier CSV 
# numit "produse.csv".

import csv
import os

csv_path = "TEME/exercitii_JSON_CSV/2_3_4/produse.csv"

produse = []

if os.path.exists(csv_path):
    with open(csv_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for rand in reader:
            produse.append(rand)


while True:
    print("\n1 - Adauga un produs")
    print("2 - Sterge un produs")
    print("3 - Afisaza produsele")
    print("4 - Exit")
    
    optiune = input("Alege optiunea: ")
    
    if optiune == "1":
        nume = input("Numele produsului: ")
        pret = input("Pretul produsului: ")
        cant = input("Cantitatea: ")
        
        produs = {
            "nume" : nume,
            "pret" : pret,
            "cantitate" : cant
        }
        
        produse.append(produs)
        print("Produsul a fost adaugat")
        
    elif optiune == "2":
        produs_sters = input("Introdu numele produsului out of stock: ")
        
        produse_updatate = [] 
        
        for produs in produse:
            if produs["nume"] != produs_sters:
                produse_updatate.append(produs)
        
        produse = produse_updatate
        print("Produsul a fost sters de pe stock")
    
    elif optiune == "3":
        for produs in produse:
            print(produs) 
    
    elif optiune == "4":
        break
    
    else:
        print("Optiune invalida")
        
 
with open(csv_path, "w", newline="", encoding="utf-8") as file:
    fieldnames = ["nume", "pret", "cantitate"] 
    writer = csv.DictWriter(file, fieldnames=fieldnames) 
    
    writer.writeheader()
    writer.writerows(produse) 
    
print("Modificarile au fost salvate in produse.csv")                            
                
                
                
# 3. Sa se scrie un program care citeste datele despre produse din fisierul "produse.csv", adauga un camp nou "pret_total" care reprezinta pretul 
# total al stocului pentru fiecare produs (pret * cantitate) si salveaza datele intr-un fisier "produse.json".


import json

json_path = "TEME/exercitii_JSON_CSV/2_3_4/produse.json"

produse_cu_pret_total = [] 

for produs in produse:
    pret = float(produs["pret"])
    cantitate = float(produs["cantitate"])
    
    produs["pret_total"] = pret * cantitate
    
    produse_cu_pret_total.append(produs) 
    
with open(json_path, "w", encoding="utf-8") as file:
    json.dump(produse_cu_pret_total, file, indent=4, ensure_ascii=False) 
    
print("produse.json a fost creat cu campul pret_total.")                         



# 4.Sa se scrie un program care citeste datele despre produse din fisierul "produse.json", adauga un camp nou "tara_origine" care reprezinta tara de origine a produsului si 
# salveaza datele intr-un fisier "produse.csv".

csv_path = "TEME/exercitii_JSON_CSV/2_3_4/produse_update.csv"

with open(json_path, "r", encoding="utf-8") as file:
    produse_json = json.load(file)
    
for produs in produse_json:
    tara = input(f"Tara de origine pentru {produs['nume']}: ") 
    produs['tara_origine'] = tara 
    
fieldnames = ["nume", "pret", "cantitate", "pret_total", "tara_origine"] 

with open(csv_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(produse_json) 
    
print("Fisierul produse_updatate.csv a fost creat cu campul tara_origine")       
 