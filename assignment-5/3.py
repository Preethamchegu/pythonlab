t=int(input("enter number of testcases:"))
for i in range(t):
    a=-1
    b=-1
    s=input("enter a string:")
    for i in range(len(s)-1,-1,-1):
        for j in range(i-1,-1,-1):
            if ord(s[i])>ord(s[j]):
                a=i
                b=j
                break
        if  a!=-1 and b !=-1:
            break
    
    if a!=-1 and b !=-1:
        g=s[b+1:a]+s[b]+s[a+1:len(s)]
        sorted_g=''.join(sorted(g))
        s=s[:b]+s[a]+sorted_g
        print(s)
    else:
        print("no answer")
