shopping=dict()
n=input("how many products:")
n=int(n)
for i in range (n):
    product=input("enter product name:")
    price=input("enter product price:")
    price=int(price)
    shopping[product]=price
f=input("how many product prices you want to check")
f=int(f)
for j in range(f):
    product=input("enter product name:")
    if ( not shopping.get(product)):
        print("product not found")
    else:
        print(shopping[product])    