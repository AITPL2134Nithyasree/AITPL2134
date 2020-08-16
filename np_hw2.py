import numpy as np
x=np.arange(6).reshape((2,3))
y=np.array([int(i) for i in input("Enter 6 numbers:").split()]).reshape((3,2))
print(x)
print(y)
print(x.shape,y.shape)
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





'''x=np.array(int(i) for i in input("Enter 6 numbers:").split())
print(x)
x=x.reshape(0,3,2)
print(x)
y=x.transpose()
print(y)'''



#2.perform 2X3 matrix, 3X2 matrix arithmatic, subtraction, multiplication