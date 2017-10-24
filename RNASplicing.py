#RNA Splicing

text = open('rosalind_splc.txt','r')

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

rnaList = []
for i in range(0, len(dnaList)):
    rnaList.append(dnaList[i].replace('T','U'))


for i in range(1, len(rnaList)):
    if rnaList[i] in rnaList[0]:
        rnaList[0] = rnaList[0].replace(rnaList[i],'')

def translation():
    return{
        'UUU': 'F',
        'UUC': 'F',
        'UUA': 'L',
        'UUG': 'L',
        'UCU': 'S',
        'UCC': 'S',
        'UCA': 'S',
        'UCG': 'S',
        'UAU': 'Y',
        'UAC': 'Y',
        'UAA': 'Stop',
        'UAG': 'Stop',
        'UGU': 'C',
        'UGC': 'C',
        'UGA': 'Stop',
        'UGG': 'W',
        'CUU': 'L',
        'CUC': 'L',
        'CUA': 'L',
        'CUG': 'L',
        'CCU': 'P',
        'CCC': 'P',
        'CCA': 'P',
        'CCG': 'P',
        'CAU': 'H',
        'CAC': 'H',
        'CAA': 'Q',
        'CAG': 'Q',
        'CGU': 'R',
        'CGC': 'R',
        'CGA': 'R',
        'CGG': 'R',
        'AUU': 'I',
        'AUC': 'I',
        'AUA': 'I',
        'AUG': 'M',
        'ACU': 'T',
        'ACC': 'T',
        'ACA': 'T',
        'ACG': 'T',
        'AAU': 'N',
        'AAC': 'N',
        'AAA': 'K',
        'AAG': 'K',
        'AGU': 'S',
        'AGC': 'S',
        'AGA': 'R',
        'AGG': 'R',
        'GUU': 'V',
        'GUC': 'V',
        'GUA': 'V',
        'GUG': 'V',
        'GCU': 'A',
        'GCC': 'A',
        'GCA': 'A',
        'GCG': 'A',
        'GAU': 'D',
        'GAC': 'D',
        'GAA': 'E',
        'GAG': 'E',
        'GGU': 'G',
        'GGC': 'G',
        'GGA': 'G',
        'GGG': 'G',
    }

rna = rnaList[0]
n=3
start = False
codons = [rna[i:i+n] for i in range(0, len(rna), n)]
aminoacids = []
ribosome = translation()

for i in range(0,len(codons)):
    if len(codons[i])<3:
        break
    aa = ribosome[codons[i]]
    if aa == 'M':
        start = True
    if start == True:
        if aa == 'Stop':
            print('stop')
            start = False
            break
        else:
            aminoacids.append(aa)

protein = ''.join(aminoacids)
print(protein)
