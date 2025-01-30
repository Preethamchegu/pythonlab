a=input("enter string:")
a=list(a)
p=str()
for i in range(len(a)):
    
    if(i%2!=0):
        s=str(a[i])
        s=s.capitalize()
        p=p+s
    else:
        p=p+a[i]    
print(p)
