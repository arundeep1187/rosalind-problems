#Independent Alleles

import math

k = 6
N = 16

x = 2**k
y = N


#Combinations Formula
def combination(a, b):
    result = math.factorial(a) / (math.factorial(b)*math.factorial(a-b))
    return result

#Creating a list of probabilities for each combination
probs = []
for i in range(y,x+1):
    thisProb=.25**i*.75**(x-i)
    probs.append(thisProb)

probTotal = 0
j = y
for i in range(0,len(probs)):
    comb = combination(x,y)
    probTotal = probTotal + probs[i]*combination(x,y)
    y = y+1

print(probTotal)
