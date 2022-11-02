a,b,c=map(int,input().split())
t=2*a*b*c*512
p=t//1024
print(p,end='KB')