class shape:
    def area(self,area):
        print(self.area)
        pass
    def perimeter(self):
        pass
class rectangle(shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        area=self.l*self.b
        print(area)
    def perimeter(self):
        perimeter=(self.l+self.b)*2
        print(perimeter)
class circle(shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        area=3.14*(self.r**2)
        print(area)
    def perimeter(self):
        perimeter=2*3.14*self.r
        print(perimeter)
s1=rectangle(5,4)
s1.area()
s1.perimeter()
s2=circle(6)
s2.area()
s1.perimeter()
          