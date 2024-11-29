T = int(input())
for _ in range(T):
    n = int(input())
    p = list(map(int,input().split()))
    print(max(p)+sum(p))
