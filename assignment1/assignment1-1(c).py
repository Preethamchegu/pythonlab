list=[]

for i in range(27):
    c=chr(96+i)
    c=c*i
    list.append(c)
    del c
print(list)
    
    
