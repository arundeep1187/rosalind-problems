#Partial Permutations

import math

n = 93
k = 8

answer = (math.factorial(n)/math.factorial(n-k))%1000000
print(int(answer))
