n=int(input())
a=0
b=1
if(n==a or n==b):
    print("Fabinacci")
else:
    next=a+b
    while(next<n):
        a=b
        b=next
        next=a+b
if(next==n):
    print("True")
else:
    print("False")