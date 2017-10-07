#Open Reading Frames

def dnaTranslation():
    return{
        'TTT': 'F',
        'TTC': 'F',
        'TTA': 'L',
        'TTG': 'L',
        'TCT': 'S',
        'TCC': 'S',
        'TCA': 'S',
        'TCG': 'S',
        'TAT': 'Y',
        'TAC': 'Y',
        'TAA': 'Stop',
        'TAG': 'Stop',
        'TGT': 'C',
        'TGC': 'C',
        'TGA': 'Stop',
        'TGG': 'W',
        'CTT': 'L',
        'CTC': 'L',
        'CTA': 'L',
        'CTG': 'L',
        'CCT': 'P',
        'CCC': 'P',
        'CCA': 'P',
        'CCG': 'P',
        'CAT': 'H',
        'CAC': 'H',
        'CAA': 'Q',
        'CAG': 'Q',
        'CGT': 'R',
        'CGC': 'R',
        'CGA': 'R',
        'CGG': 'R',
        'ATT': 'I',
        'ATC': 'I',
        'ATA': 'I',
        'ATG': 'M',
        'ACT': 'T',
        'ACC': 'T',
        'ACA': 'T',
        'ACG': 'T',
        'AAT': 'N',
        'AAC': 'N',
        'AAA': 'K',
        'AAG': 'K',
        'AGT': 'S',
        'AGC': 'S',
        'AGA': 'R',
        'AGG': 'R',
        'GTT': 'V',
        'GTC': 'V',
        'GTA': 'V',
        'GTG': 'V',
        'GCT': 'A',
        'GCC': 'A',
        'GCA': 'A',
        'GCG': 'A',
        'GAT': 'D',
        'GAC': 'D',
        'GAA': 'E',
        'GAG': 'E',
        'GGT': 'G',
        'GGC': 'G',
        'GGA': 'G',
        'GGG': 'G',
    }
text = open('rosalind_orf.txt','r')

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
ORF = []
ORF.append(dna)
ORF.append(dna[1:])
ORF.append(dna[2:])
revDNA = dna[::-1]

A = 1
C = 2
G = 3
T = 4

revCompCode = revDNA.replace('A',str(T)).replace('C',str(G)).replace('G',str(C)).replace('T',str(A))
revComp = revCompCode.replace(str(A),'A').replace(str(C),'C').replace(str(G),'G').replace(str(T),'T')

ORF.append(revComp)
ORF.append(revComp[1:])
ORF.append(revComp[2:])

n=3
proteins =[]
ribosome = dnaTranslation()
#print(ORF)
for k in range(0, len(ORF)):
    dna = ORF[k]
    codons = [dna[i:i+n] for i in range(0, len(dna), n)]
    stop = False
    mLoc = [p for p, check in enumerate(codons) if check == 'ATG']
    if len(mLoc) > 0:
        for i in range(0,len(mLoc)):
            aminoacids = []
            j = mLoc[i]
            while (stop == False):
                if j == len(codons)-1:
                    break
                aa = ribosome[codons[j]]
                if aa == 'Stop':
                    stop = True
                    proteins.append(aminoacids)
                    break
                else:
                    aminoacids.append(aa)
                j = j + 1
            stop = False

joinedProteins = []
#print(proteins)
for i in range(0,len(proteins)):
    protein = ''.join(proteins[i])
    if protein not in joinedProteins:
        joinedProteins.append(protein)
        print(protein)
