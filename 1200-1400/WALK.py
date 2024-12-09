T = int(input())
for i in range(T):
    n = int(input())
    w = list(map(int,input().split()))
    maxi = max(w)
    for i in range(n):
        if w[i] > maxi-i:
            maxi = w[i] + i 
    print(maxi)
