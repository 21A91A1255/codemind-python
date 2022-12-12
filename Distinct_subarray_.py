def fun(s):
    l=[]
    for i in range(len(s)+1):
        for j in range(i):
            l.append(s[j:i])
    return l
a=int(input())
b=int(input())
l=[]
for k in range(a,b+1):
    l.append(k)
c=0
for i in fun(l):
    if(sum(i)%2!=0):
        c+=1
print(c)