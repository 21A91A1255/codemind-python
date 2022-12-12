a=int(input())
for i in range(a):
    n=int(input())
    l=list(map(int,input().split()))
    m=list(map(int,input().split()))
    p=l+m
    l=[]
    for j in range(1,n+1):
        l.append(j)
    p=set(p)
    p=list(p)
    p.sort()
    if(p==l):
        print("YES")
    else:
        print("NO")