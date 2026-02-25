# 2.Sa se scrie un program care parcurge recursiv un folder specificat de utilizator si afiseaza calea absoluta a tuturor fisierelor ".txt".


import os 

folder = input("Introdu calea folderului: ")

for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith(".txt"):
            calea_completa = os.path.join(root, file)
            
            calea_absoluta = os.path.abspath(calea_completa)
            
            print(calea_absoluta)