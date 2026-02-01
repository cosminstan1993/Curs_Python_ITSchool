# Primește o listă de numere și grupează elementele în două liste: una cu numere negative, alta cu numere pozitive și zero.
# # Exemplu: [10,-1,2,-3,0,4,-5] -> negative: [-1,-3,-5], pozitive_si_zero: [10,2,0,4]

lista = [10, -1, 3, 4, 6, 0, 201111034]
negative = [x for x in lista if x < 0]
pozitive_si_zero = [y for y in lista if y >= 0]
print(negative)
print(pozitive_si_zero)

