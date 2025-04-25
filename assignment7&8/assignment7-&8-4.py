class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __compare__(self,other):
        if(self.salary>other.salary):
            print(f"{self.name} has greater salary than{other.name}")    
        elif(self.salary==other.salary):
            print(f"{self.name} has equal salary  than{other.name}")
        else:
            print(f"{self.name} has lower salary than {other.name}") 
    def __add__(self,other):
        print("name:",self.name+other.name)
        print("salary:",self.salary+other.salary)
    def __sub__(self,other):
        print("salary:",self.salary-other.salary)
e1=employee('pre',700)
e2=employee('hari',800)  
e1+e2  
e1-e2       