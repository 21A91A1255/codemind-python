s=input()
s=s.lower()
s1=input()
s1=s1.lower()
p=s.split()
q=s1.split()
k=[]
for i in q:
    if i in p:
        k.append(i)
print(*k)