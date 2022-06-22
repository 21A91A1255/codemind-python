n=int(input())
a=list(map(int,input().split()))
c=[]
for i in range(n):
    r=a[i]*a[i]
    c.append(r)
x=sorted(c)
y=list(x)
print(*y)