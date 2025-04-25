class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head = None
    def delete(self,num):
        temp=self.head
        prev=None
        while temp is not None and temp.data != num:
            prev=temp
            temp=temp.next
        if temp is None:
            print("not found")
            return
        elif prev is None:
            self.head=self.head.next
        else:
            prev.next=temp.next
            temp=None    
    def insertatbegin(self,num):
        new=node(num)
        new.next=self.head
        self.head=new  
    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next
l1=linkedlist()
l1.insertatbegin(3)
l1.insertatbegin(2)
l1.insertatbegin(1)
l1.delete(1)
l1.display()

