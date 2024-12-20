T = int(input())
for _ in range(T):
    N = int(input())
    p = list(map(int, input().split()))
    gd = 0
    for i in range(N):
        ans = True
        for j in range(max(0, i - 5), i):
            if p[i] >= p[j]:
                ans = False
                break
        if ans:
            gd += 1
    print(gd)
