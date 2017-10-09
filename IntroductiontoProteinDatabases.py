from urllib.request import urlopen
from re import compile

UNIPROT = 'http://www.uniprot.org/uniprot/id.txt'

def sequence_from_uniprot(name):
    url = UNIPROT.replace('id', name)
    fasta = urlopen(url)
    seq = ''.join([str(line, 'utf8').rstrip() for line in fasta.readlines()[1:]])
    return name, seq

def openText(name):
    url = UNIPROT.replace('id',name)
    parse = urlopen(url)
    return parse

biologicalProcesses = []
parse = openText('Q8R0P4')
processLine = ''
noneFound = False
while processLine[0:2] != 'DR':
    checkLine = parse.readline()
    checkLine = str(checkLine, 'utf8').rstrip()
    processLine = checkLine
    if processLine == '':
        print('No biological processes found')
        noneFound = True
        break

while processLine[5:7] != 'GO' and noneFound == False:
    checkLine = parse.readline()
    checkLine = str(checkLine, 'utf8').rstrip()
    processLine = checkLine
    if processLine == '':
        print('No biological processes found')
        noneFound = True
        break

while processLine[21:23] != 'P:' and noneFound == False:
    checkLine = parse.readline()
    checkLine = str(checkLine, 'utf8').rstrip()
    processLine = checkLine
    if processLine == '':
        print('No biological processes found')
        noneFound = True
        break

while processLine[21:23] == 'P:' and noneFound == False:
    semiLoc = [p for p, check in enumerate(processLine) if check == ';']
    biologicalProcesses.append(processLine[23:semiLoc[2]])
    checkLine = parse.readline()
    checkLine = str(checkLine, 'utf8').rstrip()
    processLine = checkLine

if noneFound == False:
    for i in range(0,len(biologicalProcesses)):
        print(biologicalProcesses[i])
