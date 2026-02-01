# 26. Primește un text și verifică dacă începe și se termină cu aceeași literă.

text = input('scrie un text: ')

if len(text) > 0 and text[0].lower() == text[-1].lower():
    print('textul incepe si se termina cu aceeasi litera')
else:
    print('nu are aceeasi litera la inceput si la final')    