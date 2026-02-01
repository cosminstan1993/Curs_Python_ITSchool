# 16. Primește un text și afișează doar literele mici din el.

text = input('introdu un text: ')
litere_mici = [p for p in text if p.islower()]
print(litere_mici)

#sau varianta cu string:

text = input('screi text: ')
litere_mici = "".join([p for p in text if p.islower()])
print(litere_mici)