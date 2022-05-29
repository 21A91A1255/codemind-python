a=int(input())
b=int(input())
s=0
k=0
temp=a
res=b
for i in range(1,a//2+1):
        if(a%i==0):
            s=s+i
#print(s)
for j in range(1,b//2+1):
        if(b%j==0):
            k=k+j
#print(k)
if(temp==k and res==s):
    print("Amicable")
else:
    print("Not Amicable")
     
    