t=input("no.of test cases:")
t=int(t)
numbers=list()
for i in range(t):
    s=input("")
    numbers.append(s)
for k in range(t):
    temp=numbers[k]
    temp=list(temp)
    numbers[k]=int(numbers[k])
    count=0
    for j in range(len(temp)):
        temp[j]=int(temp[j])
        if(numbers[k]%temp[j]==0):
            count+=1
    print(count)
        
    
