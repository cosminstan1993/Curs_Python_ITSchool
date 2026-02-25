# 6) Scrie o funcție care primește un string și returnează stringul inversat.

def invers(string):
    string = string[::-1]
    return string


string = input('scrie un text: ')

print(invers(string))