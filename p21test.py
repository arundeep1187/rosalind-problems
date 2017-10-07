def reverseCompliment(dna):
    revDNA = dna[::-1]

    A = 1
    C = 2
    G = 3
    T = 4

    revCompCode = revDNA.replace('A',str(T)).replace('C',str(G)).replace('G',str(C)).replace('T',str(A))
    revComp = revCompCode.replace(str(A),'A').replace(str(C),'C').replace(str(G),'G').replace(str(T),'T')

    return revComp

text = open('rosalind_revp.txt','r')
idList = []
dnaList = []

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


dna = dnaList[0]
positions = []
lengths = []
for i in range(0, len(dna)-3):
    confirmedPalindrome = False
    for j in range(3, 12):
        if i + j + 1 > len(dna):
            break
        pal = dna[i:i+j+1]
        if pal == reverseCompliment(pal):
            confirmedPalindrome = True
            confirmedPosition = i+1
            possibleLength = len(pal)
    if confirmedPalindrome == True:
        positions.append(confirmedPosition)
        lengths.append(possibleLength)

for i in range(0,len(positions)):
    print(str(positions[i])+ ' '+str(lengths[i]))
    test = dna[positions[i]-1:positions[i]-1+lengths[i]]
    if test != reverseCompliment(test):
        print('NOPE')
