import math
T = int(input())
for _ in range(T):
    n,d = map(int,input().split())
    a = list(map(int,input().split()))
    b,c=0,0
    for i in a:
        if i>=80 or i<=9:
            b+=1
        else:
            c+=1
    x = math.ceil(b/d)
    y = math.ceil(c/d)
    print(x+y)
