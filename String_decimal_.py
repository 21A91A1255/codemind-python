a=int(input())
for i in range(a):
    n=input()
    r=len(n)
    c=0
    p=0
    for i in range(0,r):
        p+=1
        if n[i] in '1234567890':
            c+=1
    if(p==c):
       print("True")
    else:
        print("False")
            
        