k=input("enter length in feet:")
k=int(k)
list=[k*12,k*0.33333333333,k/5280,k*304.8,k*30.48,k*0.3048,k*0.0003048]
i=input("enter num:")
i=int(i)
print(list[i-1])