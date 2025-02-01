import math
T = int(input())
for _ in range(T):
    p,s = map(int,input().split())
    l = (p-math.sqrt((p**2) - (24*s)))/12
    h = (p-8*l)/4
    print("%.2f" % (l*l*h))
