import math
n=int(input())
temp=n
s=0
q=0
i=1
while(n>0):
    r=n%10
    s=s*10+r
    n=n//10
while(s>0):
    d=s%10
    k=d**i
    #print(k)
    q=q+k
   # print(q)
    s=s//10
    i+=1
#print(r)
if(q==temp):
    print("True")
else:
    print("False")