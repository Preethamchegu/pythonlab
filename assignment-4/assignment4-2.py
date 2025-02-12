test=int(input("no. of test cases:"))
for i in range(test):
    a,b=input("enter two nums:").split()
    a=int(a)
    b=int(b)
    count=0
    for k in range(a,b+1):
        k=k**0.5
        if(k%1==0):
            count+=1
    print(count)        

