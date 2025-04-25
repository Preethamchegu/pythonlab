class Bank:
    def __init__ (self):
        self.name=['akbar','balu','chakram']
        self.acc=[101,102,1033]
        self.bal=[200,300,400]
    def search(self,d):
        b=(self.acc).index(d)
        return b
    def deposit(self,amount,b):
             self.bal[b]=self.bal[b]+amount 
    def withdrawal(self,amount,b):
          if amount<self.bal[b]:
             self.bal[b]=self.bal[b]-amount 
          else:
              print("not possible available balance is",self.bal)
    def display(self,b):
                print("name",self.name[b])
                print("account number",self.acc[b])
                print("Avl balance",self.bal[b])
testing=Bank()
b=testing.search(102)
testing.display(b)
print("\n")
testing.deposit(900,b)
testing.display(b)
print("\n")
testing.withdrawal(800,b)
testing.display(b)


    
    