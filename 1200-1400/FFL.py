T = int(input())
for _ in range(T):
    n,s = map(int,input().split())
    p = list(map(int,input().split()))
    t = list(map(int,input().split()))
    b,d=[],[]
    for i in range(n):
        if t[i] == 0:
            b.append(p[i])
        elif t[i] == 1:
            d.append(p[i])
    if len(b)==0 or len(d)==0:
        print("no")
    else:
        if s+min(b)+min(d) <= 100:
            print("yes")
        else:
            print("no")
