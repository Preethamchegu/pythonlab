class convertor:
    k=0
    def __init__(self,l,u):
        self.l=l
        self.u=u
        if(u=='inches'):
            convertor.k=l
        elif(u=='feet'):
            convertor.k=l*12    
        elif(u=='miles'):
            convertor.k=l*63360  
        elif(u=='kilometers'):
            convertor.k=l*39370.1   
        elif(u=='meters'):
            convertor.k=l*39.37    
        elif(u=='centimeters'):
            convertor.k=l*0.3937    
        elif(u=='millimeters'):
            convertor.k=l*0.03937   
    def inches(self):
        print(convertor.k)
    def feet(self):
        print(convertor.k/12)
    def miles(self):
        print(convertor.k/63360)
    def kilometers(self):
        print(convertor.k/39370.1)
    def meters(self):
        print(convertor.k/39.37)
    def centimeters(self):
        print(convertor.k/0.3937)
    def milliimeters(self):
        print(convertor.k/0.03937)         
p1=convertor(6,'meters') 
p1.centimeters()  
   
        