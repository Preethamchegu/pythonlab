import math
class vector:
    def __init__(self,p,q):
        self.p=p
        self.q=q
    def mag(self):
        m=(self.p**2+self.q**2)**0.5  
        return m
    def rotation(self):
        return math.degrees(math.atan2(self.p,self.q))
class _2D_vector:
    def __init__(self,x,y,a,b):
        self.x=x
        self.y=y
        self.a=a
        self.b=b
    def dot_product(self):
        return (self.x)*(self.a)+(self.y)*(self.b)
    def vector_product(self):
        return (self.x)*(self.b)-(self.y)*(self.a)
class _3D_vector(_2D_vector):
    def __init__(self,x,y,z,a,b,c):
        self.x=x
        self.y=y
        self.a=a
        self.b=b
        self.z=z
        self.c=c
    def dot_product(self):
        return (self.x)*(self.a)+(self.y)*(self.b)+(self.z)*(self.c)
    def vector_product(self):
        return (self.y)*(self.c)-(self.b)*(self.z),(self.a)*(self.z)-(self.c)*(self.x),(self.x)*(self.b)-(self.y)*(self.a),
c=vector(2,3)
print(c.rotation)
a=_2D_vector(3,4,3,5)
print(a.dot_product())
print(a.vector_product(),"in the direction of z axis")
b=_3D_vector(3,4,5,2,3,5)
print(b.dot_product())
x,y,z=b.vector_product()
print(x,"x-axis",y,"Y-axis",z,"z-axis")