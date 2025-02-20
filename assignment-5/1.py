a=int(input("enter small number:"))
b=int(input("enter larger number:"))
c=0
s=[]
g=[]
for i in range(a,b+1):
    for j in range(i,b+1):
        if c<(i^j):
            s=[]
            g=[]
            s.append(i)
            g.append(j)
            c=i^j
        elif c==(i^j):
            s.append(i)
            g.append(j)
        else :
            pass
print("the highest value of xor",list(zip(s,g)),"=",c)
