a=int(input())
n=input()
x=''
for i in n:
    if(i==' '):
        continue
    else:
        x=x+i
x=int(x)
y=str(x+1)
for i in y:
    print(i,end=' ')
