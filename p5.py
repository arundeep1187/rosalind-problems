#Computing GC Content

text = open('rosalind_gc.txt','r')

def GCContent(dna):
    aCount = 0
    gCount = 0
    cCount = 0
    tCount = 0

    for i in range(0,len(dna)):
      if dna[i]=="A":
        aCount = aCount + 1
      elif dna[i]=="G":
        gCount = gCount + 1
      elif dna[i]=="C":
        cCount = cCount + 1
      elif dna[i]=="T":
        tCount = tCount + 1
      else:
        print("ERROR invalid nucleobase")
        print("error value: "+str(i))

    GC = (gCount+cCount)/(aCount+gCount+cCount+tCount)
    return GC


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


same = []
m = 0
maxInitialized = False

for i in range(0,len(dnaList)):
    current = GCContent(dnaList[i])*100
    if not maxInitialized:
        m = current
        same.append(i)
        maxInitialized = True
    elif m < current:
        m = current
        same = []
        same.append(i)
    elif m == current:
        same.append(i)

m = format(m, '.6f')
print(idList[same[0]]+ "\n"+str(m))
