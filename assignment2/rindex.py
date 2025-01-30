str=input("string:")
ser=input("string searching for:")
lind=len(str)-1
pen=len(ser)
flag=0
for i in range(len(str)):
    if(str[lind-i:(lind-i)-pen:-1]==ser[::-1]):
        print((lind-i)-pen+1)
        flag=1
       
if(flag==0):
    print('-1')        
    