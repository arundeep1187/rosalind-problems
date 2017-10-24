#Mendel's First Law

k=22
m=26
n=19
t = k + m + n

KK = 1
KM = 1
KN = 1
MM = .75
MN = .5
NN = 0


kkprob = k/t * (k-1)/(t-1) * KK
kmprob = k/t * m/(t-1) * KM * 2
knprob = k/t * n/(t-1) * KN *2
mmprob = m/t * (m-1)/(t-1) * MM
mnprob = m/t * n/(t-1) * MN * 2
nnprob = n/t * (n-1)/(t-1) * NN

totalProb = (kkprob + kmprob + knprob + mmprob + mnprob + nnprob)
print(totalProb)
