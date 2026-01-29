# 12. Primește un text și verifică dacă este palindrom.

text = input('introdu ce vrei tu da vezi sa fie la fel si de la capat: ')
textul_clean = "".join(c.lower() for c in text if c.isalnum())
if textul_clean == text[::-1]:
    print('e la fel si invers')
else:
    print('ai gresit tu ceva')    
