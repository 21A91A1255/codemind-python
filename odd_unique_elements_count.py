n=int(input())
a=list(map(int,input().split()))
q=set(a)
p=list(q)
c=0
for i in range(len(p)):
    if(p[i]%2!=0):
        c+=1
print(c)