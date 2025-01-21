T = int(input())
for i in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    print(len(set(a)))
