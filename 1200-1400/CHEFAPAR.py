T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    count = a.count(0)
    due = 0 
    for i in range(n):
        if a[i] == 0:
            due = n-i
            break
    print((count*1000)+(due*100))
