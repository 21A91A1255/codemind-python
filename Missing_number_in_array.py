n=int(input())
for i in range(n):
    m=int(input())
    a=list(map(int,input().split()))
    l=[]
    for i in range(1,m+1):
        l.append(i)
    for i in l:
        if i not in a:
            print(i)
          