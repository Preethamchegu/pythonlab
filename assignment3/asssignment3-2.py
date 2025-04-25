def fibo(num):
    if num==1 or num==0:
        return 1
    else:
        
        return fibo(num-2)+fibo(num-1)
    
test=int(input("enter no of test cases:"))   
list=[]
for i in range(test):
    value=int(input("enter value:"))
    num=0
    while(value>fibo(num)):
        num+=1
    if(value==fibo(num)):
        a="is a fibo"
        list.append(a)
    else:
        a="is not a fibo"
        list.append(a) 
for i in list:
    print(i)        

    
