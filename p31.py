#Transitions and Transversions

text = open('rosalind_tran.txt','r')

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

s1 = dnaList[0]
s2 = dnaList[1]

transitionCount = 0
transversionCount = 0

for i in range(0,len(s1)):
    if s1[i] != s2[i]:
        if s1[i]=='A' or s1[i]=='G':
            if s2[i]=='A' or s2[i]=='G':
                transitionCount = transitionCount + 1
            elif s2[i]=='C' or s2[i]=='T':
                transversionCount = transversionCount + 1
            else:
                print('ERROR')
        elif s1[i]=='C' or s1[i]=='T':
            if s2[i]=='C' or s2[i]=='T':
                transitionCount = transitionCount + 1
            elif s2[i]=='A' or s2[i]=='G':
                transversionCount = transversionCount + 1
            else:
                print('ERROR')
        else:
            print('ERROR')

ratio = transitionCount/transversionCount
print(ratio)
