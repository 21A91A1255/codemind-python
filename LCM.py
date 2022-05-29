a,b=map(int,input().split())
k=0
c=b
while(c):
    k+=1
    if c%a==0 and c%b==0:
       print(c)
       break 
    c+=1

               
