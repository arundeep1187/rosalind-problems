#Mortal Fibonacci Rabbits

n=99
k=1
m=20

x=[0]*n

for i in range(0,n):
    if i<=1:
        x[i]=1
    else:
        x[i]=x[i-1]+k*x[i-2]
    if i>=m:
        x[:] = [a - x[i-m] for a in x]

print(x[n-1])
