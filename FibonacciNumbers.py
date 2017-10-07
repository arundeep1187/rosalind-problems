#Rabbits and Recurrence Relations ft. Fibonacci Numbers

n=5
k=3

x=[0]*n

for i in range(0,n):
  if i<=1:
     x[i]=1
  else:
    x[i]=x[i-1]+k*x[i-2]

print(x[n-1])
