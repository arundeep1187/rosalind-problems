#Consensus and Profile

text=open('rosalind_cons.txt','r')

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


n = len(dnaList[0])
print(n)
matA=[]
matC=[]
matG=[]
matT=[]

for i in range(0,n):
    a = 0
    c = 0
    g = 0
    t = 0
    for j in range(0,len(idList)):
        if dnaList[j][i]=='A':
            a = a+1
        if dnaList[j][i]=='G':
            g = g+1
        if dnaList[j][i]=='C':
            c = c+1
        if dnaList[j][i]=='T':
            t = t+1
    matA.append(a)
    matC.append(c)
    matG.append(g)
    matT.append(t)

approx = []
for i in range(0,n):
    check = max(matA[i],matC[i],matG[i],matT[i])
    if check == matA[i]:
        new = 'A'
    elif check == matC[i]:
        new = 'C'
    elif check == matG[i]:
        new = 'G'
    elif check == matT[i]:
        new = 'T'
    else:
        print('error 404')

    approx.append(new)

A = ' '.join(str(x) for x in matA)
C = ' '.join(str(x) for x in matC)
G = ' '.join(str(x) for x in matG)
T = ' '.join(str(x) for x in matT)
ancestor = ''.join(approx)
print(ancestor)
print('A: '+A)
print('C: '+C)
print('G: '+G)
print('T: '+T)
