T = int(input())
for _ in range(T):
    n,k = map(int,input().split())
    f = list(map(str,input().split()))
    m = []
    for i in range(k):
        p = list(map(str,input().split()))
        m.extend(p)
    for j in f:
        if j in m:
            print("YES", end = " ")
        else:
            print("NO", end = " ")
    print()
