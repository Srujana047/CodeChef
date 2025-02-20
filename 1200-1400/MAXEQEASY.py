t = int(input())
for _ in range(t):
    n = int(input())
    ar = list(map(int,input().split()))
    st = set(ar)
    ct = []
    for i in st:
        if i > 0:
            ct.append(ar.count(i))
    ct.sort()
    z = ar.count(0)
    s = 0
    if z == 0 or len(ct) == 0:
        for i in ct:
            s += int((i*(i-1))/2)
        s += int((z*(z-1))/2)
    else:
        ct[-1] += z
        for i in ct:
            s += int((i*(i-1))/2)
    print(s)
