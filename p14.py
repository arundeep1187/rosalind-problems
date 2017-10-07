#Independent Alleles

import math

k = 6
N = 16

x = 2**k
y = N

#notes
'''mixing +AaBb
if AABB then .5 * .5
if AABb then .5 * .5
if AAbb then .5 * .5
if AaBB then .5 * .5
if AaBb then .25
if Aabb then .5 * .5
if aaBB then .5 * .5
if aaBb then .5 * .5
if aabb then .5 * .5

a= .25 * .75 * .75 * .75 * .75 * .75 * (6C1)
b= .25 * .25 * .75 * .75 * .75 * .75 * (6C2)
c= .25 * .25 * .25 * .75 * .75 * .75 * (6C3)
d= .25 * .25 * .25 * .25 * .75 * .75 * (6C4)
e= .25 * .25 * .25 * .25 * .25 * .75 * (6C5)
f= .25 * .25 * .25 * .25 * .25 * .25 * (6C6){1}

gen1
.75 * .75
.75 * .25
.25 * .25 * 2'''

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
