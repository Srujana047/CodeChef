import math
T = int(input())
for i in range(T):
    x,y = map(int,input().split())
    z = math.gcd(x,y)
    print(2*z)
