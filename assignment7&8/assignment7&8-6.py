#Create a class "BankAccount" with attributes account number and balance. 
# Implement #methods to deposit and withdraw funds, and a display method to show the account details.
class Bankaccount:
    def __init__(self,accnum,bal):
        self.accnum=accnum
        self.bal=bal
    def withdraw(self,am):
        if am<=self.bal:
            self.bal-=am
        else:
            print("not possible")
    def deposit(self,am):
        self.bal+=am
    def display(self):
        print(f"account number:{self.accnum}")  
        print(f"balance:{self.bal}")  
p=Bankaccount(1234,2400)
p.deposit(500)
p.withdraw(200)
p.display()
