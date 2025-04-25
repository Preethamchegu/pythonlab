import numpy as np
# n=int(input("n:"))

# while True:
#     l=np.random.randint(1,n**2,n)
#     if np.sum(l)==n*(n**2+1)/2:
#         print(l)
#         break
# while True:
#     k=[]
#     for i in range(n*n):
#         f=np.random.choice(l)
#         k.append(f)      
#     k=np.array(k)
#     k=k.reshape(n,n)
#     r=np.sum(k,axis=0)
#     c=np.sum(k,axis=1)
#     r=r-34
#     c=c-34
#     if not c.any():
#         if not r.any():
#             print(k)
#             break
import numpy as np

def generate_magic_square(n):
    if n % 2 == 1:  # Odd-order magic square
        magic_square = np.zeros((n, n), dtype=int)
        num = 1
        i, j = 0, n // 2  
        while num <= n * n:
            magic_square[i, j] = num
            num += 1
            i -= 1 
            j += 1  
            
            if num % n == 1:  
                i += 2
                j -= 1
            elif i < 0:  
                i = n - 1
            elif j == n:  
                j = 0
    
    else:
         magic_square = np.arange(1, n*n + 1).reshape(n, n)
    swap = np.zeros((n, n), dtype=bool)

    for i in range(n):
        for j in range(n):
            if (i % 4 == j % 4) or ((i + j) % 4 == 3):
                swap[i, j] = True

    selected_elements = magic_square[swap]
    magic_square[swap] = selected_elements[::-1]
    
    return magic_square

# Generate magic squares for N=4, 5, 6, 7, 8
# for size in [4, 5, 6, 7, 8]:
#     print(f"\nMagic Square for N={size}:")
k=int(input("enter size:"))
print(generate_magic_square(k))



