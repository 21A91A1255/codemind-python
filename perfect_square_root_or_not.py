import math
n=int(input())
temp=n
k=math.sqrt(n)
#print(k)
r=int(k)*int(k)
#print(r)
q=n-r
if(q==0):
    print("True")
else:
    print("False")