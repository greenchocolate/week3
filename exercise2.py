import numpy as np
from scipy import interpolate
from scipy import optimize

#read data
with open("ENyYffaq.txt") as matrix_file:
    a = np.loadtxt(matrix_file,delimiter=' ')
    matrix_file.close()
[n,m]=a.shape

#set x and y
x=a[:n,0]
y=a[:n,1]

#interpolate
f=interpolate.interp1d(x,y,kind='cubic')

#use fsolve to find roots
roots1=optimize.fsolve(f,-3)
print(roots1)
print(f(roots1[0]))
roots2=optimize.fsolve(f,3)
print(roots2)
print(f(roots2[0]))

#plot function and data points
import matplotlib.pyplot as plt
x1=np.linspace(-20,19,200)
y1=np.empty([200,])

for i in range(200):
    y1[i]=f(x1[i])
print(x1.shape)
print(y1.shape)
plt.plot(x1,y1,color='blue',linestyle='--')
plt.scatter(x,y,color='red')
plt.plot(x,np.zeros(x.shape),color='black')

plt.show()
