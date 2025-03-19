T = int(input())
for i in range(T):
    n = list(map(int,input().split()))
    a = set(map(int,input().split()))
    b = set(map(int,input().split()))
    x = a.difference(b)
    print(n[0]-len(x))
