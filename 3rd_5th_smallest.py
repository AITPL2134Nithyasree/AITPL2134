print("Enter atleast 5 numbers")
l=[int(i) for i in input().split()]#reading the input
l.sort()
if len(l)>=5:
    print("3rd smallest is:{0} and 5th smallest is:{1}".format(l1[2],l1[4]))
elif len(l)>=3:
    print("3rd smallest is:",l[2]," length less than 5,we cann't find 5th smallest")
else:
    print("please enter atleast 3 numbers")
