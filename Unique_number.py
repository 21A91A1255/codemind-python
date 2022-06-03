n=int(input())
n=str(n)
m=list(set(n))
n=list(n)
if len(n)==len(m):
    print("Unique Number")
else:
    print("Not Unique Number")