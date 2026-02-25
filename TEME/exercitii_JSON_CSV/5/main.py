# 5.Se da urmatoarea structura de directoare care contine informatii despre elevii dintr-o scoala:
# school_files/high_school/classA - contine fisiere CSV cu informatii despre elevii de la filologie
# school_files/high_school/classB - contine fisiere JSON cu informatii despre elevii de la mate-info 
#  Sa se scrie un program care parcurge recursiv structura de directoare "school_files" si:
# -Afiseaza toti elevii din clasele de Filologie (ClassA) care au nota peste 90 la Istorie
# -Afiseaza toti elevii din clasele de Mate-Info (ClassB) care au media mai mica deca 80
# -Calculeaza media generala a tuturor claselor de Filologie
# -Afiseaza clasele de Mate-info in ordine crescatoare a mediei generale pe clasa
# -Afiseaza elevii cu cea mai mare medie din fiecare clasa
# -Convertește fisierele csv in care sunt salvate informatiile despre elevii de la Filologie in fisiere json.
# -Convertește fisierele json in care sunt salvate informatiile despre elevii de la Mate-Info in fisiere csv.


import os 
import json
import csv

path_classA = "TEME/exercitii_JSON_CSV/5/school_files/high_school/classA"
path_classB = "TEME/exercitii_JSON_CSV/5/school_files/high_school/classB"

#================FILOLOGIE====================


medii_fililogie = []

for file in os.listdir(path_classA):
    
    if file.endswith(".csv"):
        
        path = os.path.join(path_classA, file)
        
        with open(path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            
            suma = 0
            nr = 0
            max_media = 0 
            top_elev = ""
            
            for elev in reader:
                
                geo = float(elev["Geography"])
                eng = float(elev["English"])
                hist = float(elev["History"])
                
                media = (geo + eng + hist) / 3
                
                if hist > 90:
                    print("Filologie - Istorie >90: ", elev["Name"])
                    
                suma += media
                nr += 1
                    
                if media > max_media:
                        max_media = media
                        top_elev = elev["Name"]
                        
            media_clasa = suma / nr
            medii_fililogie.append(media_clasa)
            
            print("Top elev Filologie", file, ":", top_elev)
            
print("\nMedia generala Filologie: ", sum(medii_fililogie) / len(medii_fililogie)) 

#===========================MATE-INFO=======================================

medii_mate_info = {} 

for file in os.listdir(path_classB):
    
    if file.endswith(".json"):
        
        path = os.path.join(path_classB, file) 
        
        with open(path, "r", encoding="utf-8") as file:
            elevi = json.load(file)
            
            suma = 0 
            max_media = 0 
            top_elev = ""
            
            for elev in elevi:
                
                grades = elev["grades"]
                
                media = ((grades["math"] + grades["english"] + grades["science"]) / 3)
                
                if media < 80:
                    print("Mate-Info - media <80:", elev["name"])
                    
                suma += media
                
                if media > max_media:
                    max_media = media
                    top_elev = elev["name"]
                    
            medie_clasa = suma / len(elevi) 
            medii_mate_info[file] = medie_clasa
            
            print("Top elev Mate-Info", file, ":", top_elev)          
            
            
print("\nClase Mate-Info sortate crescator: ")

for clasa, medie in sorted(medii_mate_info.items(), key=lambda x: x[1]):
    print(clasa, medie)            
            
             