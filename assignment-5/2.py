t=int(input("enter number of testcases:"))
for i in range(t):
    k=int(input("enter number cuts to be done:"))
    print("maximum number of 1*1 chocalate bars is",(k//2)*(k-(k//2)))
