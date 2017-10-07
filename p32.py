#Completing a Tree
import numpy as np

text=open('rosalind_tree.txt','r')

x = []
y = []
minEdges = 0

deadLeaves = []
deadNodes = []
deadInternalNodes = []

current = text.read().splitlines()
n=int(current[0])
for i in range(1,len(current)):
    a= current[i].split()
    x.append(int(a[0]))
    y.append(int(a[1]))

total = x + y
degreeList = np.zeros(n)
disconnectedNodes = []

for i in range(1,n+1):
    degrees = total.count(i)
    if degrees == 0:
        disconnectedNodes.append(i)
        deadNodes.append(i)
        minEdges = minEdges + 1
    degreeList[i-1] = degrees

#print(disconnectedNodes)
#print(degreeList)
iLoc= [p for p, check in enumerate(degreeList) if check >= 2]
internalNodes = np.array(iLoc)+1

#print(internalNodes)

leaves = [v for v, v in enumerate(list(range(1,n+1))) if v not in internalNodes and v not in disconnectedNodes]
#print(leaves)


internalNodes = list(internalNodes)
for i in range(0,len(internalNodes)):
    #print(internalNodes)
    xLoc = [v for v, check in enumerate(x) if check == internalNodes[i]]
    yLoc = [v for v, check in enumerate(y) if check == internalNodes[i]]

    if internalNodes[i] == 1:
        print('sup')
        print(xLoc)
        print(yLoc)
    internalConnection = []
    path = []
    degrees = degreeList[internalNodes[i]-1]
    if len(xLoc)!=0:
        for j in range(0,len(xLoc)):
                if y[xLoc[j]] in leaves:
                    degrees = degrees - 1
                else:
                    internalConnection.append(y[xLoc[j]])
                    path.append(y[xLoc[j]])
    if len(yLoc)!=0:
        for j in range(0,len(yLoc)):
                if x[yLoc[j]] in leaves:
                    degrees = degrees - 1
                else:
                    internalConnection.append(x[yLoc[j]])
                    path.append(x[yLoc[j]])



    if degrees == 0:
        disconnectedNodes.append(internalNodes[i])
        deadInternalNodes.append(internalNodes[i])
    else:
        path.append(internalNodes[i])
        while(len(internalConnection) != 0):
            xLoc = [v for v, check in enumerate(x) if check == internalConnection[0]]
            yLoc = [v for v, check in enumerate(y) if check == internalConnection[0]]

            degrees = degreeList[internalConnection[0]-1]
            if len(xLoc)!=0:
                for j in range(0,len(xLoc)):
                        if y[xLoc[j]] in leaves:
                            degrees = degrees - 1
                        elif y[xLoc[j]] in path:
                            degrees = degrees - 1
                        else:
                            internalConnection.append(y[xLoc[j]])
                            path.append(y[xLoc[j]])

            if len(yLoc)!=0:
                for j in range(0,len(yLoc)):
                        if x[yLoc[j]] in leaves:
                            degrees = degrees - 1
                        elif x[yLoc[j]] in path:
                            degrees = degrees - 1
                        else:
                            internalConnection.append(x[yLoc[j]])
                            path.append(x[yLoc[j]])
            print(path)
            if degrees == 0:
                if internalConnection[0] in path:
                    print(internalConnection[0])
                    if set(disconnectedNodes).isdisjoint(path):
                        disconnectedNodes.append(internalConnection[0])
                        deadInternalNodes.append(internalConnection[0])
                        internalNodes.remove(internalConnection[0])
                        internalConnection.remove(internalConnection[0])
                    else:
                        internalNodes.remove(internalConnection[0])
                        internalConnection.remove(internalConnection[0])
                else:
                    disconnectedNodes.append(internalConnection[0])
                    deadInternalNodes.append(internalConnection[0])
                    internalNodes.remove(internalConnection[0])
                    internalConnection.remove(internalConnection[0])
            else:
                #if internalConnection[0]==2:
                    #print(path)
                #print(internalConnection[0])
                internalNodes.remove(internalConnection[0])
                internalConnection.remove(internalConnection[0])

    if len(internalNodes) == i+1:
        break


checkLeaves = leaves
while (len(checkLeaves)!= 0):
    xLoc = [v for v, check in enumerate(x) if check == checkLeaves[0]]
    yLoc = [v for v, check in enumerate(y) if check == checkLeaves[0]]

    if len(xLoc)!=0:
        if y[xLoc[0]] in leaves:
            disconnectedNodes.append(checkLeaves[0])
            deadLeaves.append(checkLeaves[0])
            checkLeaves.remove(y[xLoc[0]])
            checkLeaves.remove(checkLeaves[0])
        else:
            checkLeaves.remove(checkLeaves[0])
    elif len(yLoc)!=0:
        if x[yLoc[0]] in leaves:
            disconnectedNodes.append(checkLeaves[0])
            deadLeaves.append(checkLeaves[0])
            checkLeaves.remove(x[yLoc[0]])
            checkLeaves.remove(checkLeaves[0])
        else:
            checkLeaves.remove(checkLeaves[0])

#print(disconnectedNodes)
print('Dead Leaves = '+str(deadLeaves))
print('Dead Nodes = '+str(deadNodes))
print('Dead Internal Nodes = '+str(deadInternalNodes))
print(len(disconnectedNodes)-1)
easy = n - 1 - len(x)
print('Easy Solution = n - 1 - given edges = '+ str(easy))
