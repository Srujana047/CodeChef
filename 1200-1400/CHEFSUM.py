T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    minimum = min(a)
    print(a.index(minimum) +1 )
