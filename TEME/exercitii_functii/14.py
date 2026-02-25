# 13) Scrie o functie care primeste o lista de numere si returneaza un dictionar cu frecventa fiecarui numar in 
# lista (cheia este numarul, valoarea este frecventa).
numere = [10, 20, 10, 20, 30, 40, 30, 40, 50]   
def frecventa_numere(lista):
    dictionar = {}
    for x in lista :
        if x in dictionar:
            dictionar[x] = dictionar[x] + 1
        else:
            dictionar[x] = 1 
    return dictionar


rezultat = frecventa_numere(numere)
               
print(rezultat)    