import numpy as np
x=np.array([int(i) for i in input("Enter 8 numbers:").split()]).reshape((4,2))
y=x.transpose()
if x.shape==y.shape:
    print("sum of matrices:")
    print(x+y)
    print("-----------")
    print("subtraction of matrices:")
    print(x-y)
    print("-----------")
else:
    print("Addition & subtraction are not possible.")
if x.shape[1]==y.shape[0]:
    print("Multiplication is:")
    print(x.dot(y))
    print("-----------")
else:
    print("Multiplication is not possible.")




#4.x=4X2, convert to--> x transpose=2X4, perform all arithmatic operations
