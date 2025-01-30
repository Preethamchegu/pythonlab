str=input("enter string:")
ser=input("which string want to search")
count=0
for i in range(len(str)-len(ser)+1):
    if(str[i:i+len(ser)] == ser):
       count+=1
print(count)    