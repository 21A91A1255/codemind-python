def prime(n):
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0
    else:
        return 1
        
        
n=int(input())
m=int(input())
x=m+n
temp=x
while(1):
    if prime(x+1):
        y=x+1
        break
    x+=1
print(y-temp)