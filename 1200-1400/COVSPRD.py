import math
T = int(input())
for i in range(T):
    n,d = map(int,input().split())
    if d==0:
        print(1)
    elif d<=10:
        print(min(2**d,n))
    elif d<=20:
        print(min(1024*pow(3,(d-10)),n))
    else:
        print(n)
