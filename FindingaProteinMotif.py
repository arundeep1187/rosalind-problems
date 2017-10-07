#Finding a Protein Motif

from Bio import ExPASy
from Bio import SwissProt

text = open('rosalind_mprt.txt','r')

idList = []
currentID = 'blank'
while currentID != '':
    currentID = text.readline()
    if currentID == '':
        break
    currentID = currentID.replace('\n','')
    idList.append(currentID)

#note: inefficient method for retrieving sequences
sequenceList = []
for i in range(0,len(idList)):
    h = ExPASy.get_sprot_raw(idList[i])
    r = SwissProt.read(h)
    sequenceList.append(r.sequence)

#check for N-glycosylation motif - N{P}[ST]{P}
motifList = []
for i in range(0,len(idList)):
    n = 'N'
    nLoc= [p for p, check in enumerate(sequenceList[i]) if check == n] #find all locations for N
    subMotifList = []
    for j in range(0,len(nLoc)):
        if nLoc[j]+3 <= len(sequenceList[i])-1:
            if sequenceList[i][nLoc[j]+1] != 'P':
                if sequenceList[i][nLoc[j]+2] == 'S' or sequenceList[i][nLoc[j]+2] == 'T':
                    if sequenceList[i][nLoc[j]+3] != 'P':
                        subMotifList.append(nLoc[j]+1)

    motifList.append(subMotifList)

for i in range(0,len(idList)):
    if len(motifList[i]) > 0:
        print(idList[i])
        motifs = ' '.join(str(x) for x in motifList[i])
        print(motifs)
