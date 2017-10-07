#Finding a Spliced Motif

import numpy as np

text = open('rosalind_sseq.txt','r')

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

indices = []
initialized = False
for i in range(0,len(dnaList[1])):
    f = dnaList[1][i]
    fLoc= np.array([p for p, check in enumerate(dnaList[0]) if check == f]) +1

    if initialized == False:
        indices.append(fLoc[0])
        initialized = True
    else:
        for i in range(0,len(fLoc)):
            if fLoc[i]>indices[len(indices)-1]:
                indices.append(fLoc[i])
                break

indices = ' '.join(str(x) for x in indices)
print(indices)
