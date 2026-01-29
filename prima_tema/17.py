# 17. Primește două numere și afișează toate numerele între ele (inclusiv), în ordine crescătoare.

a = int(input('introdu primul numar: '))
b = int(input('introdu al doilea numar: '))

start = min(a, b)
end = max(a, b)

for n in range(start, end +1):
    print('numerele cuprinse intre a si be sunt: ', n)

#sau

a = int(input('introdu primul numar: '))
b = int(input('introdu al doilea numar: '))

start = min(a, b)
end = max(a, b)

rezultat = " ".join(str(n) for n in range(start, end + 1))
print('numerele cuprinse intre a si b sunt:', rezultat)