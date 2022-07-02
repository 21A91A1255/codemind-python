n=int(input())
a=list(map(int,input().split()))
c=0
k=0
for i in range(n):
    k+=1
    if(a[i]==1 or a[i]==0):
        c+=1
if(k==c):
    print("True")
else:
    print("False")