n=input()
a=0
r=[]
lower=set('abcdefghijklmnopqrstuvwxyz')
for i in range(len(n)):
    if n[i] in lower:
        k=n.count(n[i])
        if(k>=1):
            a+=1
            r.append(n[i])
#print(r)
t=set(r)
print(len(t))