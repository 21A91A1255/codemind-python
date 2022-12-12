n=int(input())
l=list(map(int,input().split()))
s=1
for i in range(len(l)):
    s=s*l[i]
for j in range(len(l)):
    print(s//l[j],end=' ')