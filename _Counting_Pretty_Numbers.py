def pr(q):
    v=0
    while q:
        x=q%10
        if(x==2 or x==3 or x==9):
            v+=1
        break
    if v==1:
        return 1
    else:
        return 0
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    c=0
    for j in range(a,b+1):
        if pr(j):
            c+=1
    print(c)