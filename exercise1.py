import numpy as np
#read file
with open("XAhwshXe.txt") as matrix_file:
    a = np.loadtxt(matrix_file,delimiter=',')
    matrix_file.close()
[n,m]=a.shape
#set A=mat and b
mat=a[:n,:m-1]
b=a[:n,m-1]
#solve Ax=b
x=np.linalg.solve(mat,b)
#print error
print(abs(np.matmul(mat,x)-b))
