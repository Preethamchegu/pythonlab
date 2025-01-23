points=list()
point1=list()
point2=list()
main=list()
for i in range(10):
    a=input("enter coordinates of point:").split()
    a[0]=int(a[0])
    a[1]=int(a[1])
    a[2]=int(a[2])         
    points.append(a)
for i in range(10):
    point1=points[i]
    short=list()
    short.append(point1)
    min_distance=float('inf')
    for j in range(10):
        if (i!=j):    
            point2=points[j]
            d=0
            for k in range(3):                                                                      
                d=d+(point1[k]-point2[k])**2
            d=d**0.5
            if(min_distance>d):
                nearest_point=point2                  
                min_distance=d
                
    short.append(nearest_point)          
    main.append(short) 
    del short        
print(main)