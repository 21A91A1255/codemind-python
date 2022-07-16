def fun(n):
    t=n
    s=0
    while(n):
        d=n%10
        s=s*10+d
        n//=10
    if s==t:
        return True
    else:
        return False
a=int(input())
b=int(input())
for i in range(a,b):
    if fun(i):
        print(i,end=' ')