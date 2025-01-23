T = int(input())
for i in range(T):
    n = int(input())
    c = 0
    while(n>=0):
        if n%7==0:
            c = 1
            print(n)
            break
        n-=4
    if c==0: print('-1')
