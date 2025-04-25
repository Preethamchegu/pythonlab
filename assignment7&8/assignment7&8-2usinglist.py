maxsize=100
class qu:
    def __init__(self):
        self.rear=-1
        self.front=-1
        self.l=[]
class function:
    q=qu()
    def push(self,num):
        if(self.q.rear!=maxsize-1 ):
            self.q.rear+=1
            self.q.l.append(num)
    def pop(self):
        self.q.front+=1
        print("deleted element:",self.q.l[self.q.front])
    def display(self):
        while  self.q.front!= self.q.rear:
             self.q.front+=1
             print(self.q.l[self.q.front])
hi=function()
hi.push(5)
hi.push(7)
hi.push(9)
hi.push(56)
hi.push(57)
hi.push(4)
hi.pop()
hi.display()

