print("Enter atleast 4 numbers")
l=[int(i) for i in input().split()]
l.sort()
l1=l[::-1]
if len(l)>=4:
    print("2rd largest is:{0} and 4th largest is:{1}".format(l1[1],l1[3]))
elif len(l)>=2:
    print("2rd largest is:",l[1]," length less than 4,we cann't find 4th largest")
else:
    print("please enter atleast 2 numbers")

