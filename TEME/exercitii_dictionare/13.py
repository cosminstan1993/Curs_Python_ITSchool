# 13) Creeaza un nou dictionar care sa contina doar persoanele cu varsta peste 18 ani.

dict = {'Daniel' : 26, 
        'Radu' : 19, 
        'Matei' : 17,
          'Eugen' : 34,
            'Maria' : 24
        }


adultii = {}

for nume, varsta in dict.items():
    if varsta > 18:
       adultii[nume] = varsta
print(adultii)        


#dictionary coprehension (varu' chatgpt version):

adultii = {nume: varsta for nume, varsta in dict.items() if varsta > 18}
print(adultii)