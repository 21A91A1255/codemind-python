n=[]
n=input()
r=len(n)
k=0
c=0
for i in range(0,r):
    for j in range(i+1,r):
        k+=1
        if(n[i]==n[j]):
            c+=1
#print(k)
#print(c)
if(c==0):
    print("True")
else:
    print("False")