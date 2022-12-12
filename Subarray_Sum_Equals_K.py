def fun(s):
    l=[]
    for i in range(len(s)+1):
        for j in range(i):
            l.append(s[j:i])
    return l
a,b=map(int,input().split())
l=list(map(int,input().split()))
c=0
s=[]
for i in fun(l):
    if(sum(i)==b):
        c+=1
print(c)