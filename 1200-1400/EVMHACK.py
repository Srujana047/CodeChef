T = int(input())
for i in range(T):
    a,b,c,p,q,r = map(int,input().split())
    total = (p+q+r)/2
    x = p+b+c
    y = a+q+c
    z = a+b+r
    if (x > total) or (y>total) or (z>total):
        print("Yes")
    else:
        print("No")
