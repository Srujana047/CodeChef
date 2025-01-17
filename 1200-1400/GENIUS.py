T = int(input())
for i in range(T):
    n,x = map(int,input().split())
    if x > 3*n: 
        print("NO")
        continue
    a = (x + 2)//3 
    b = 3*a - x
    if a + b <= n: 
        print("YES")
        print(a, b, n - (a + b))
    else:
        print("NO")
