n=int(input())
m=int(input())
for i in range(n,m,1):
    c=0
    for j in range(1,m):
        if(i%j==0):
            c+=1
    if(c==2):
        print(i)
            