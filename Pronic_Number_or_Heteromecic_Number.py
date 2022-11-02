n=int(input())
c=0
for i in range(1,n-1):
    t=i*(i+1)
    if(t==n):
        c+=1
if(c==1):
    print("YES")
else:
    print("NO")