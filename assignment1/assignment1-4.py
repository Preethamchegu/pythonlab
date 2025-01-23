list0=list()
list1=list()
list2=list()
list3=list()
list4=list()
for i in range(10000):
    if((i+1)%5==0):
        list0.append(i+1)  
    elif((i+1)%5==1):
        list1.append(i+1) 
    elif((i+1)%5==2):
        list2.append(i+1) 
    elif((i+1)%5==3):
        list3.append(i+1)     
    elif((i+1)%5==4):
        list4.append(i+1)
print(list0)                  


