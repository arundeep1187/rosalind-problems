#Finding a Shared Motif

import time
import numpy as np

t0 = time.time()

text=open('rosalind_lcsm.txt','r')

idList = []
dnaList = []

#read Rosalind FASTA files
currentLine = text.readline()
lastLine = currentLine
while currentLine != '':
    currentLine = currentLine.replace('\n','')
    if '>' in currentLine:
        currentLine = currentLine.replace('>','')
        idList.append(currentLine)
        currentLine = text.readline()
        currentLine = currentLine.replace('\n','')
        lastLine = currentLine
    else:
        currentLine = text.readline()
        currentLine = currentLine.replace('\n','')
        if '>' in currentLine:
            dnaList.append(lastLine)
        elif currentLine == '':
            dnaList.append(lastLine)
            break
        else:
            currentLine = lastLine + currentLine
            lastLine = currentLine

LCS = ''
commonSubstrings = []

#replace DNA with coded list
codedDNAList = []
for i in range(0,len(dnaList)):
    code = dnaList[i].replace('A','1')
    code = code.replace('G','2')
    code = code.replace('C','3')
    code = code.replace('T','4')
    code = list(map(float,code))
    code = np.array(code)
    codedDNAList.append(code)

#x coordinate = dna1, y coordinate = dna2
if len(codedDNAList[0])>=len(codedDNAList[1]):
    dna2 = codedDNAList[0]
    dna1 = codedDNAList[1]
    primeStrand = 0

else:
    dna2 = codedDNAList[1]
    dna1 = codedDNAList[0]
    primeStrand = 1


#find substring matches, divide each row of horizontal sequence by
#each position in vertical sequence to find matches (1s)
parse = []
parse1 = []
for i in range(0,len(dna2)):
    test = dna1/dna2[i]
    test[test!=1]=0   #change all non-matches into zeroes
    parse1.append(test)

#create 2D array
parse = np.vstack(parse1[0:len(parse1)])

#connect substring matches
match = np.where(parse == 1)
for i in range(0,len(match[0])):
    check = [match[0][i],match[1][i]]
    if(check[0]!=0) and (check[1]!=0):
        if(parse[check[0]-1,check[1]-1]>0):
            parse[check[0],check[1]]=parse[check[0],check[1]]+parse[check[0]-1,check[1]-1]

largest = np.amax(parse)
maxes = np.where(parse==largest)

#create list of substrings from largest common substrings by moving backwards
#from highest to lowest matches and flipping for correct sequence
for i in range(0,len(maxes[0])):
    check = maxes[0][i]
    substring = dnaList[primeStrand][check]
    x = largest - 1
    c = 1
    while (x > 0):
        substring = substring + dnaList[primeStrand][check-c]
        x = x - 1
        c = c + 1

    substring = substring[::-1]
    commonSubstrings.append(substring)

#add substrings from smaller common substrings
if (largest > 2):
    findMore = largest - 1
    while (findMore > 1):
        nextMax = np.where(parse==findMore)
        for i in range(0,len(nextMax[0])):
            check = nextMax[0][i]
            substring = dnaList[primeStrand][check]
            x = findMore - 1
            c = 1
            while (x > 0):
                substring = substring + dnaList[primeStrand][check-c]
                x = x - 1
                c = c + 1

            substring = substring[::-1]
            commonSubstrings.append(substring)
        findMore = findMore - 1

#remove duplicates
seen = {}
commonSubstrings = [seen.setdefault(x, x) for x in commonSubstrings if x not in seen]


#test common substrings on rest of DNA strings
fail = True
x = 2
y = 0
while (x < len(idList)):
    if (x>2):
        if (LCS not in dnaList[x]):
            commonSubstrings.remove(LCS)
            if (len(commonSubstrings)==0):
                LCS = 'fail'
                fail = True
                break
            x = 2
    y = 0
    while (y < len(commonSubstrings)):
        if(commonSubstrings[y] not in dnaList[x]):
            commonSubstrings.remove(commonSubstrings[y])
            y = y - 1
            if (len(commonSubstrings)==0):
                LCS = 'fail'
                fail = True
                break

        else:
            LCS = commonSubstrings[y]
            fail = False
            break
        y = y+1

    if(fail == True):
        LCS = 'fail'
        break
    x = x + 1


print(LCS)
t1 = time.time()
total = t1-t0
print(total)
