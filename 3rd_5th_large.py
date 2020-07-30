n=int(input("Enter how many numbers you are going to enter"))
l=[]
for i in range(n):
    l.append(int(input()))

l.sort()
l1=l[::-1]
if len(l)>=5:
    print("3rd largest is:{0} and 5th largest is:{1}".format(l1[2],l1[4]))
elif len(l)>=3:
    print("3rd largest is:",l[2]," you have given only {0} numbers".format(len(l)))
else:
    print("please enter atleast 3 numbers")
