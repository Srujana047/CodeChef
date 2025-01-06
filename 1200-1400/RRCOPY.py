T = int(input())
for i in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    x = set(a)
    print(len(x))
