n = int(input("Enter the no.of rows:"))

for i in range(n):
    k=1
    for j in range(n-i-1):
        print(end="  ")
    for j in range(i+1,i+i+2):
        print(k,end=" ")
        if k==1:
            k=0
        else:
            k=1
    for j in range(2*i,i,-1):
        print(k,end=" ")
        if k==1:
            k=0
        else:
            k=1
    print()
