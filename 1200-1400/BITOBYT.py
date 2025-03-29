T = int(input())
for i in range(T):
    n = int(input())
    r = (n-1) % 26
    q = (n-1) // 26
    if r < 2:
        print(2**q, 0,0)
    elif r < 10:
        print(0, 2**q, 0)
    else:
        print(0, 0, 2**q)
