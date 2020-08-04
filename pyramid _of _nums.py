n = int(input("Enter the no.of rows:"))
for i in range(n):
    for j in range(n-i-1):
        print(end="  ")
    for j in range(i+1,i+i+2):
        print(j,end=" ")
    for j in range(2*i,i,-1):
        print(j,end=" ")
    print()
    
