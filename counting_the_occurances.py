n=input()
p=input()
k=0
for i in range(len(n)):
    if(n[i]==p):
        k+=1
if(k==0):
    print("-1")
else:
    print(k)