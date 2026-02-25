# 1.Sa se scrie un program care parcurge recursiv un folder specificat de utilizator si afiseaza numele tuturor fisierelor cu extensia ".py".

import os

folder = input("Introdu calea folderului: ")

for rood, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith(".py"):
          print(file)