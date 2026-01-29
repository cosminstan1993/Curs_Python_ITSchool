# 1. Citeste varsta unei persoane si afisaza daca este major sau minor.

# varsta = int(input('introdu varsta: '))

# if varsta >= 18:
#     print('persoana este majora')

# else:
#     print('persoana nu este majora')


# - input() -> citeste varsta de la tastatura ca text. 
# - int() -> o transforma in numar. 
# - if -> verifica daca varsta este cel putin 18. 
    

# 2. Verifica daca un numar este multiplu de 10.

# numar = int(input('introdu un numar: '))

# if numar % 10 == 0:
#     print('numarul este multiplu de 10')

# else:
#     print('numarul nu este multiplu de 10')    


# 3.Citește o notă (1–10) și afișează:
# „Insuficient” (<5)
# „Suficient” (5–6)
# „Bine” (7–8)
# „Foarte bine” (9–10)


# nota = int(input('introdu o nota: '))

# if nota < 5:
#     print('insuficient')
# elif nota <= 6: 
#     print('suficient')
# elif nota <= 8:
#     print('bine')
# else:
#     print('foarte')         



# 4. Citeste un caracter si verifica daca este litera sau cifra.

# caracter = input('introdu un caracter: ')

# if caracter.isdigit():
#     print('caracterul este o cifra')
# elif caracter.isalpha():
#     print('caracterul este o litera')
# else:
#     print("caracterul nu este nici litera nici numar")        




# 5. Citesete n si afisaza numerele de la 1 la n.

# n = int(input('introdu un numar: '))

# for i in range(1, n + 1):
#     print(i)



# 6. Calculeaza suma numerelor de la 1 la n.


#PRIMA VARIANTA:
# n = int(input('introdu un numar: '))
# suma = n * (n + 1) // 2 
# print(suma)

# #A DOUA VARIANTA:
# n = int(input('introdu un numar" '))
# suma = 0 
# for i in range(1, n+ 1):
#     suma += i
# print(suma)    

# 7. Afisaza toate numerele pare de la 1 la n. 

# n = int(input('introdu n: '))
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         print(i)


# 8. Afisaza tabla inmultirii cu un numar dat. 

n = int(input("introdu un numar: "))

for i in range(1, n + 1):
    print(f"{n} x {i} =  {n * i}")


# 9. Citeste un numar si afisaza cate cifre are. 

# 10. Citeste un text si numara vocalele. 

# 11. Afisaza textul citit invers. 

# 12. Verifica daca un cuvant este palindrom. 

# 13. Verifica daca un text are:
#     - cel putin 8 caractere
#     - o litera mare
#     - o cifra 

# 14. Afisaza toti divizorii unui numar. 

# 15. Verifica daca un numar este prim. 

# 16. Afisaza toate numerele intre 1 si n care sunt divizibile cu 3 sau cu 7. 