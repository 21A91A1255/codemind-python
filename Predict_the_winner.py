n=int(input())
sum=0
sum1=0
arr=list(map(int,input().split()))
for i in range(n//2):
    sum=sum+arr[i]
for i in range(n//2,n):
    sum1=sum1+arr[i]
a=abs(sum-sum1)
if a%4==0:
    print("X")
else:
    print("Y")