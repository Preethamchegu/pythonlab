list=[]
a=int(input("enter no of test cases:"))
for i in range (a):
    n=int(input("enter no. of growth cycles:"))
    height=1
    j=0
    while(j<n):
        if(j%2 == 0):
            height*=2 
        else: 
            height+=1
        j+=1       
    list.append(height) 
for i in list:  
    print(i)        
