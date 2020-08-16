import numpy as np
a=[int(i) for i in input("Enter 4 diagonal elemnts of matrix:").split()]
x=np.diag(a)
y=np.array([int(i) for i in input("Enter 8 numbers:").split()]).reshape((4,2))
print("diagonal matrix:")
print(x)
print("4X2 matrix:")
print(y)
print("Multiplication Matrix:")
print(x.dot(y))




#3.Create a diagonal matrix and multiply it with 4X2 matrix
