class Password_manager:
    old_password=[]
    n=0
    def get_password(self):
        if(Password_manager.n==0):
            print("no password yet")
        else:
            print(Password_manager.old_password[-1])  
    def set_password(self,pas):
        if(Password_manager.old_password.count(pas)==0):
            Password_manager.old_password.append(pas)
            Password_manager.n += 1
        elif(Password_manager.old_password.count(pas)==1):
            Password_manager.old_password.remove(pas)
            Password_manager.old_password.append(pas)
    def is_correct(self,pas):
        if(Password_manager.old_password[-1]==pas):
            print('true')
            return True
        else:
            print('false')
            return False
            
p1=Password_manager()
p1.set_password('hi')
p1.set_password('hello')
p1.set_password('how')
print(Password_manager.old_password)
p1.is_correct('how')
