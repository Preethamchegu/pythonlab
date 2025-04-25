# 4. Take N (N >= 10) random 2-dimensional points represented in cartesian coordinate space.  Store them in a numpy array. Convert them to polar coordinates. 
import numpy as np
n=int(input("no. of vectors:"))
p=[]
for i in range(n):
    print("vector",i+1,sep=" ",end="")
    k=[]
    k=input(":").split()
    for j in range(2):
        k[j]=int(k[j])
    p.append(k)
p=np.array(p)
p=p**2
print(p)
mag=np.sum(p,axis=1)
print(mag)
mag=mag**0.5
print(mag)
ang=np.arccos(p[0]/mag)
print(ang)































































































        