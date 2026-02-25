from menu import *

while True:
    try:
        print("1.Adaugare elev")
        print("2.Afisare elevi")
        print("3.Stergere elev")
        print("4.Media descrescatoare")
        print("5.Media peste 8")
        print("6.Alfabetic")
        print("0.Iesire")

        opt = input("Alege: ")

        if opt == "1":
            adauga()
        elif opt == "2":
            afisaza()
        elif opt == "3":
            sterge()
        elif opt == "4":
            dupa_medii()
        elif opt == "5":
            peste8()
        elif opt == "6":
            alfabetica()
        elif opt == "0":
            break
        else:
            print("Optiune invalida\n")

    except Exception as e:
        print("Eroare:", e)
        print("Programul continua...\n")
        
