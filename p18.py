#Enumerating Gene Orders

import math as m
import itertools

n = 6
print(m.factorial(n))

factorial = []
for i in range(0, n):
    factorial.append(i+1)

permutations = list(itertools.permutations(factorial))

for i in range(0,len(permutations)):
    string = ' '.join(str(x) for x in permutations[i])
    print(string)
