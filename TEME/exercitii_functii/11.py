# 11) Scrie o functie care primeste un dictionar de forma {nume: varsta} si returneaza un dictionar cu persoanele care au 
# varsta peste 18 ani.

def persoane_majore(dictionar):
    persoanele_majore = {}
    for nume, varsta in dictionar.items():
        if varsta >= 18:
            persoanele_majore[nume] = varsta
    return persoanele_majore
   


persoane = {}
n = int(input('cate persoane vrei sa introduci?: ')) 

for i in range(n):
    nume = input('introdu un nume: ')
    varsta = int(input(f'introdu varsta pentru {nume}: '))
    persoane[nume] = varsta   

#sau 


persoane = {}

def filtru(persoane):
    rezultat = {}
    for nume, varsta in persoane.items():
        if varsta >= 18:
            rezultat[nume] = varsta
    return rezultat
        
   

while True:
    date = input('introdu date: ')
    if date == "stop":
        break
    date_clean = date.split(" ")
    nume = date_clean[2]
    varsta = int(date_clean[-1])
    persoane[nume] = varsta


print("persoanele majore sunt: ", filtru(persoane))