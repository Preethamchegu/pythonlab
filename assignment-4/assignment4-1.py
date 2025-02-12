test=int(input("no. of test cases:"))
res=[]
for i in range(test):
    str=input("enter string:")
    f=len(str)
    let=list(str)
    count=0
    for l in range(f//2):
            if (let[l]>let[f-1-l]):
                count+=(ord(let[l])-ord(let[f-1-l]))
            elif (let[l]<let[f-1-l]):
                count+=(ord(let[f-1-l])-ord(let[l]))
    print(count)
