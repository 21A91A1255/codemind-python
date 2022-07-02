n=input()
for j in n.split():
    s=j
    x=0
    a=100000
    for i in s:
        if ord(i)>x:
            x=ord(i)
        if ord(i)<a:
            a=ord(i)
    print(chr(a),chr(x),end=' ')