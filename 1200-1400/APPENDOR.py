T = int(input())
for i in range(T):
    n,y = map(int, input().split())
    a = list(map(int, input().split()))
    bit = a[0]
    for num in a: 
        bit |= num 
    if y == bit|y:
        print(y - bit)
    else:
        print(-1)   
