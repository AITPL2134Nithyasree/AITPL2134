n=int(input())
c=0
for i in range(1,n):
    if n%i==0:      #checks 'i' is a factor of 'n' or not
        c+=1
if c==1:
    print("yes, the given number is a prime number")
else:
    print("no, the given number is not a prime")
