n=int(input())
res=0
while(res!=1 and res!=4):
        res=0;
        while(n>0):
                d=n%10
                res=res+(d*d)
                n=n//10
        n=res
if(res==1):
    print("True")
else:
    print("False")
            