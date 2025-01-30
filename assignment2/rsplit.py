def split(text,punct,times):
     a=[] 
     b=[]
     start=0

     for i in range(len(text)):
          if(text[i]==' '): 
               a.append(text[start:i:])
               start=i
     b=a[:len(a)-times]          
     bes= ' '.join(b)
     print(bes,end='')
     for i in range(len(a)-times,len(a)):
          print(",",a[i],end='')
str=input("enter sentence with space:")
times=input("enter how many times split from last:") 
times=int(times)         
split(str,',',times-1 )



            
