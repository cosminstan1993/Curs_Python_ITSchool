# Exerciții de vacanță – recapitulare Python (variabile, operatori, stringuri, control flow)
# Perioada: 23 decembrie – 11 ianuarie

# Încălzire (1-10):
# 1. Creează două variabile cu valori numerice și afișează suma lor.

# a = 10
# b = 26

# suma = a + b
# print(suma)


# 2. Afișează produsul a două numere introduse de la tastatură.

# a = int(input('introdu primul numar '))
# b = int(input('introdu al doilea numar '))

# produs = a * b 
# print('produsul este:' , produs)


# 3. Primește un nume de la tastatură și afișează-l cu litere mari.

# nume = input("Introdu un nume: ")
# print(nume.upper())


# 4. Afișează lungimea unui string introdus de la tastatură.

# text = input("Introdu un string: ")
# print(len(text))


# 5. Verifică dacă un număr este par sau impar.

# numar = int(input("Introdu un numar: "))

# if numar % 2 == 0:
#     print("Numarul este par")
# else:
#     print("Numarul este impar")


# 6. Primește un text și un caracter, afișează de câte ori apare caracterul în text.

# text = input('Introdu textul: ')
# caracter = input('introdu un caracter: ')

# print(text.count(caracter))


# 7. Afișează ultimul caracter dintr-un string introdus de la tastatură.

# text = input('introdu un string: ')
# print(text[-1])

# 8. Primește un număr și afișează dacă este pozitiv, negativ sau zero.

# numar = float(input('introdu un numar: '))

# if numar > 0:
#     print('Numarul este pozitiv')

# elif numar < 0: 
#     print('Numarul este negativ')

# else: 
#     print('Numarul este zero')


# 9. Afișează toate caracterele unui string, câte unul pe linie.

# text = input('Introdu un string: ')

# for caracter in text:
#       print(caracter)

  

# 10. Primește două numere și afișează cel mai mare dintre ele.

# a = float(input('introdu primul numar: '))
# b = float(input('introdu al doilea numar: '))

# if a > b:
#     print(a)

# elif a < b:
#     print(b)



# Exerciții pentru oameni incalziti (11-30):
# 11. Primește trei numere și afișează cel mai mic dintre ele.

# a = float(input('introdu primul numar: '))
# b = float(input('introdu al doilea numar: '))
# c = float(input('introdu al treilea numar: '))

# if a <= b and a <= c:
#     print(a)

# elif b <= c and b <= a:
#     print(b)

# else:
#     print(c)

# 12. Primește un text și verifică dacă este palindrom.

# text = input('introdu un text: ')

# clean_text = text.replace(" ", "").lower()

# if clean_text == clean_text[::-1]:
#     print("textul este palidorm")
# else:
#     print('textul nu este palidrom')

# 13. Primește o parolă și verifică dacă are cel puțin 8 caractere și conține o cifră.

# parola = input('introdu o parola: ')

# lungimea_parolei = len(parola) >= 8 
# contine_cifra = any(caracter.isdigit() for caracter in parola)

# if lungimea_parolei and contine_cifra:
#     print('parola este valida')

# else:
#     print('parola este invalida')    


# 14. Primește un text și construiește un nou string numai cu vocalele din el.

# text = input('introdu un text: ')

# vocale = 'aeiouAEIOU'
# rezultat = ""

# for caracter in text: 
#     if caracter in vocale:
#         rezultat += caracter


# print('stringul cu vocale: ' , rezultat)



# 15. Primește un număr n și afișează toate numerele pare de la 0 la n (inclusiv).

# n = int(input('introdu un numar: '))

# for p in range(0, n + 1):
#     if p % 2 == 0:
#         print(p) 
    

# 16. Primește un text și afișează doar literele mici din el.

# text = input('introdu textul: ')

# for caracter in text: 
#     if caracter.islower():
#         print(caracter)


# text = input('introdu textul; ')

# rezultat = ""
# for caracter in text:
#     if caracter.islower():
#         rezultat += caracter

# print(rezultat)        


# 17. Primește două numere și afișează toate numerele între ele (inclusiv), în ordine crescătoare.

# a = int(input('introdu primul numar: '))
# b = int(input('introdu al doilea numar: '))

# start = min(a, b)
# end = max(a, b)

# for n in range(start, end + 1):
#     print('nnumerele cuprinse intre a si b sunt: ', n)



# 18. Primește un text și afișează fiecare cuvânt pe o linie nouă.

# text = input('introdu un text: ')

# cuvinte = text.split()

# for cuvant in cuvinte:
#     print(cuvant)



# 19. Primește un număr și afișează tabla înmulțirii pentru acel număr (de la 1 la 10).   


# n = int(input('introdu un numar: '))

# for i in range(1, 11):
#     print(n, 'x', i, '=', n * i)



# 20. Primește un text și verifică dacă toate caracterele sunt litere mici.

# text = input('introdu un text: ')

# if text.islower():
#     print('toate caracterele sunt litere mici ')

# else:
#     print('nu toate caracterele sunt litere mici ')


# 21. Primește un text și afișează-l inversat.

# text = input('introdu un text: ')

# text_invers = text[::-1]
# print(text_invers)


# 22. Primește o propoziție și numără câte cuvinte conține.

# propozitie = input('introdu un text: ')

# cuvinte = propozitie.split()
# print(len(cuvinte))


# 23. Primește un text și înlocuiește toate spațiile cu caracterul "_".

# text = input("introdu un text: ")

# text_modificat = text.replace(" ", "_")
# print(text_modificat)



# 24. Primește un număr și afișează suma cifrelor sale.

# n = input('introdu un numar: ') 

# suma = 0
# for cifra in n:
#     suma += int(cifra)

# print(suma)    


# 25. Primește un text și afișează doar caracterele care sunt cifre.

# text = input('introdu un text: ')

# for caracter in text:
#     if caracter.isdigit():
#         print(caracter, end="")



# 26. Primește un text și verifică dacă începe și se termină cu aceeași literă.


# text = input('introdu un text: ')

# text = text.strip()

# if len(text) > 0 and text[0].lower() == text[-1].lower():
#     print('textul incepe si se termina cu aceeasi litera')

# else: 
#     print("textul NU incepe si NU se termina cu aceeasi litera")


# 27. Primește un text și afișează toate caracterele distincte din el.

# text = input()

# caractere_distincte = set(text)

# for caracter in caractere_distincte:
#     print(caracter, end="")


# 28. Primește un text și afișează literele care apar de exact două ori.

# text = input()

# litere = {}

# for caracter in text: 
#     if caracter.isalpha():
#         if caracter in litere:
#             litere[caracter] += 1

# else:
#     litere[caracter] = 1

# for caracter, count in litere.items():
#     if count == 2:
#         print(caracter, end='')    


# 29. Primește un număr n și afișează toți divizorii săi../

# n = int(input('introdu un numar: '))

# print('divizorii lui', n, 'sunt:')

# for i in range (1, n + 1):
#     if n % i == 0:
#         print(i)



# 30. Primește un text și verifică dacă are cel puțin o literă mare, una mică și o cifră.

# text = input('introdu un text: ') 

# are_litera_mare = False 
# are_lietra_mica = False
# are_cifra = False

# for caracter in text:
#     if caracter.isupper():
#         are_litera_mare = True
#     elif caracter.islower():
#         are_litera_mica = True 
#     elif caracter.isdigit():
#         are_cifra = True


# if are_litera_mare and are_lietra_mica and are_cifra:
#     print('textul este valid')

# else:
#     print('textul NU este valid')    


# Exercitii pentru oameni supraincalziti (31-33):
# 31. Fizz Buzz: Primește un număr n și afișează numerele de la 1 la n. Pentru multiplii de 3, afișează "Fizz", pentru multiplii de 5, afișează "Buzz", iar pentru multiplii de ambele, afișează "FizzBuzz".

# x = int(input('introdu un text: '))

# for n in range(1, n + 1):
#     if n % 3 == 0 and n % 5 == 0:
#         print('fizzbuzz')




# 32. Primește un text și afișează-l cu fiecare cuvânt inversat, dar în aceeași ordine. (Exemplu: "Ana are mere" -> "anA era erem")
# 33. Primește un text care contine o insiruire de numere și afișează media lor. (Exemplu: "1,2,3,4,5,10" -> 25/6 = 4.1666)

# Spor la exersat și sărbători fericite!
