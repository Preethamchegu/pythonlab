import random
list=[]
max=[]
count=0
for i in range(100):
    list.append(random.randint(0,1))
print(list)    
for i in range(100):
    if list[i]==0 and list[i+1]==0:
        count+=1
    else:
        max.append(count+1)
        count=0
k=len(max) 
maximum=max[0]           
for i in range(k-1):
    if(maximum<max[i]):
        maximum=max[i]
print(maximum)
