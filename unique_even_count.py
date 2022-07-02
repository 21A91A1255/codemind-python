n=int(input())
a=list(map(int,input().split()))
p=set(a)
q=list(p)
c=0
for i in range(len(q)):
    if(q[i]%2==0):
        c+=1
print(c)