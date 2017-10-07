#Overlap Graphs

text = open('rosalind_grph.txt','r')

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

print(idList)
print(dnaList)

k = 3
for i in range(0,len(dnaList)):
    suffix = dnaList[i][len(dnaList[i])-k:len(dnaList[i])]
    for j in range(0, len(dnaList)):
        prefix = dnaList[j][0:k]
        if i != j:
            if suffix == prefix:
                print(idList[i],idList[j])
