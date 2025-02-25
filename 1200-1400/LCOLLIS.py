T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    x = [0] * m
    for i in range(n):
        s = input()
        for j in range(m):
            if s[j] == '1':
                x[j] += 1
    c = 0
    for y in x:
        if y>1:
            c += (y*(y-1))//2
    print(c)
