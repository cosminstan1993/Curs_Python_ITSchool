# 11. Primește trei numere și afișează cel mai mic dintre ele.


unu = int(input('primul numar: '))
doi = int(input('al doilea numar: '))
trei = int(input('al treilea numar: '))

if unu >= doi and trei >= doi:
    print(doi)
elif doi >= trei and doi >= trei:
    print(trei)
else:
    print(unu)