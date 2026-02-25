#  5)Scrie o functie care primeste ca parametru un numar si modifica valoarea unei variabile globale cu valoarea numarului
#  la patrat.

var = " "

def func(a):
   global var 
   var = a * a 

numarul_tau = int(input('scrie un numar: '))

func(numarul_tau)
print(f' numarul la patrat este : {var}')