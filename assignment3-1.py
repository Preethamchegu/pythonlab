def sum(num):
    sum=0
    while num!=0:
        sum=sum+num%10
        num=num//10
    return sum    

num=input("enter number:")
num=int(num)
while num>9:
    num=sum(num)
print("digital root:",num)
