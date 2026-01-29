# 13. Primește o parolă și verifică dacă are cel puțin 8 caractere și conține o cifră.

parola = input("pune o parola: ")

lungime_parola = len(parola) >= 8
contine_cifra = any(c.isdigit for c in parola)

if lungime_parola and contine_cifra:
    print('parola e buna')
else:
    print("parola e slaba")