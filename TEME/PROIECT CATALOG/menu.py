from storage import citeste_elevi, salveaza_elevi

def media(e):
    return (e[2] + e[3] + e[4]) / 3

def adauga():
    elevi = citeste_elevi()
    nume = input("Introdu un Nume: ")
    prenume = input("Introdu Prenume: ")
    ro = float(input("Introdu nota la Romana: "))
    mate = float(input("Introdu nota la Matematica: "))
    eng = float(input("Introdu nota la Engleza: "))
    elevi.append([nume, prenume, ro, mate, eng])
    salveaza_elevi(elevi)
    print("Elev adaugat!\n")

def afisaza():
    elevi = citeste_elevi()
    for e in elevi:
        print(e[0], e[1], "media:", round(media(e),2))
    print()

def sterge():
    elevi = citeste_elevi()
    nume = input("Numele elevului: ")
    prenume = input("Prenumele elevului: ")
    elevi = [e for e in elevi if not (e[0]==nume and e[1]==prenume)]
    salveaza_elevi(elevi)
    print("Elev sters!\n")

def peste8():
    elevi = citeste_elevi()
    for e in elevi:
        if media(e) > 8:
            print(e[0], e[1], round(media(e),2))
        else:
            print("Nici-un elev nu are media peste 8.")    
    print()

def alfabetica():
    elevi = citeste_elevi()
    elevi.sort(key=lambda x: x[0])
    for e in elevi:
        print(e[0], e[1])
    print()

def dupa_medii():
    elevi = citeste_elevi()
    elevi.sort(key=lambda x: media(x), reverse=True)
    for e in elevi:
        print(e[0], e[1], round(media(e),2))
    print()
