T = int(input())
for _ in range(T):
    n = int(input())
    s = input()
    x = y = False
    for i in range(n):
        if s[i]=='1':
            if i%2:
                x = True
            else:
                y = True
    print(1 if x&y else 2)
