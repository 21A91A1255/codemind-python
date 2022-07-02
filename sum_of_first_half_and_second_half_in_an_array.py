n=int(input())
a=list(map(int,input().split()))
r=n//2
p=0
s=0
res=0
for i in range(0,r):
    s=s+a[i]
for j in range(r,n):
    p=p+a[j]
print(s)
print(p)
