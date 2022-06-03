n=int(input())
a=[]
p=0
a=list(map(int,input().split()))
for i in range(0,n):
    c=0
    while(a[i]>0):
        r=a[i]%10
        c+=1
        a[i]//=10
    if c%2==0:
        p+=1
print(p)