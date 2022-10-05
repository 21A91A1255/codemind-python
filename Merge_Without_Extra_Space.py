n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    p=list(map(int,input().split()))
    q=list(map(int,input().split()))
    w=p+q
    w.sort()
    print(*w)