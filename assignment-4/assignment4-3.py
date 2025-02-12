import re
sent=input("enter sentence in a small case:")
f=len(sent)
flag=0
count=0
for i in range(26):
    a=chr(97+i)
    if sent.find(a)!=-1:
        count+=1   
    else:
        flag+=1
if count==26:
    print("is a pangram")
else:
    print("not a pangram")     

