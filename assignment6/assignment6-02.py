import random
class rps:
    win=[]
    def __init__(self,n):
        self.n=n
        pass
    def computer_choice(self):
        p=random.randint(1,3)
        if(p==1):
            g='rock'
        elif(p==2):
            g='paper'
        elif(p==3):
            g='scissor' 
        return g        
    def game(self):
        i=0
        for i in range (self.n):
          g=self.computer_choice()
          print("round",i+1,end='')
          v=input(":")
          
          if(v=='rock'):
              if(g=='scissor'):
                rps.win.append('win')
              else:
                rps.win.append('lose')
          elif(v=='paper'):
              if(g=='rock'):
                rps.win.append('win')
              else:
                rps.win.append('lose')
          elif(v=='scissor'):
              if(g=='paper'):
                rps.win.append('win')
              else:
                rps.win.append('lose')  
          else:
             print("enter valid value")
p1=rps(5)
p1.game()  
print(p1.win)         

            
              
        
