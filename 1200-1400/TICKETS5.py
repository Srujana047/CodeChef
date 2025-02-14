T = int(input())
for i in range(T):
    s = input()
    x = set(s)
    if len(x) == 2:
        print('YES')
    else:
        print('NO')
