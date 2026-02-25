FILE = "TEME/PROIECT CATALOG/elevi.txt"

def citeste_elevi():
    elevi = []
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            for linie in f:
                nume, prenume, ro, mate, eng = linie.strip().split(";")
                elevi.append([nume, prenume, float(ro), float(mate), float(eng)])
    except FileNotFoundError:
        pass
    return elevi

def salveaza_elevi(elevi):
    with open(FILE, "w", encoding="utf-8") as f:
        for e in elevi:
            f.write(f"{e[0]} {e[1]}, Nota Romana:{e[2]}, Nota Matematica:{e[3]}, Nota Engleza:{e[4]}\n")

