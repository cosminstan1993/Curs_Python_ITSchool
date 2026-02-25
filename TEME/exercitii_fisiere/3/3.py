# 3. Se da urmatorul fisier "produse.txt" care contine informatii despre produse.
#    Sa se scrie un program care citeste informatiile despre produse din fisierul "produse.txt"
#    si calculeaza pretul total al stocului pentru fiecare produs.

with open("TEME/exercitii_fisiere/3/produse.txt", "r", encoding="utf-8") as f:
    linii = f.readlines()

for linie in linii:
    linie = linie.strip()  
    if linie == "":
        continue

  
    nume, pret_str, cantitate_str = linie.split(" - ")

    pret = float(pret_str.replace("lei", "").strip())
    cantitate = int(cantitate_str.replace("bucati", "").strip())

    pret_total = pret * cantitate

    print(f"{nume}: Pret total stoc = {pret_total} lei")
