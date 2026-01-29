# 16) Afiseaza toate persoanele grupate dupa decadele varstei (0-9, 10-19, 20-29, etc.).


dict = {'Daniel' : 26, 
        'Radu' : 19, 
        'Matei' : 17,
          'Eugen' : 34,
            'Maria' : 24
        }


grupa1 = []
grupa2 = []
grupa3 = []
grupa4 = []


for nume, varsta in dict.items():
   if varsta > 0 and varsta <= 10:
      grupa1.append(nume)
   elif varsta > 10 and varsta <= 20:
      grupa2.append(nume)
   elif varsta > 20 and varsta <= 30:
      grupa3.append(nume)
   elif varsta > 30 and varsta <= 40:
      grupa4.append(nume)

print('Persoanele cu varsta cuprinsa intre 0-10 ani: ', grupa1)              
print('Persoanele cu varsta cuprinsa intre 10-20 ani: ', grupa2) 
print('Persoanele cu varsta cuprinsa intre 20-30 ani: ', grupa3) 
print('Persoanele cu varsta cuprinsa intre 30-40 ani: ', grupa4) 

# #sau


 