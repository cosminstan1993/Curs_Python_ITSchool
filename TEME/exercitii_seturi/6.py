# 6) Afișează toate culorile din primul set care nu sunt în al doilea set.

set = {'albastru', 'rosu', 'galben', 'portocaliu', 'verde'}
set2 = {'maro', 'fosforescent', 'verde'}

diferente = set2.difference(set)
print(diferente)