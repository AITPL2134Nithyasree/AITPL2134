print("Enter the numbers between which primes has to display:")
m,n=input().split()
m=int(m)
n=int(n)
for j in range(m+1,n):
    c=0
    for i in range(1,j):
        if j%i==0:      #checks 'i' is a factor of 'n' or not
            c+=1
    if c==1:
        print(j,end=" ")
