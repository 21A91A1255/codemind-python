n=int(input())
a=list(map(int,input().split()))
q=set(a)
p=list(q)
s=0
for i in range(len(p)):
    s=s+p[i]
print(s)