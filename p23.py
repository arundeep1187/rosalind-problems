#Enumerating k-mers Lexicographically
import itertools

symbols = 'A B C D E'
listSym = list(symbols)

listSym = [x.strip(' ') for x in listSym]
listSym = list(filter(None,listSym))
listSym.sort()

n = 4

strings = [p for p in itertools.product(listSym, repeat=n)]

for i in range(0, len(strings)):
    currentString = ''.join(strings[i])
    print(currentString)
