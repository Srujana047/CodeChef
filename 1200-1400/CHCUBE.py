T = int(input())
for i in range(T):
    s = list(map(str, input().split()))
    if s[2] == s[0] == s[5]:
        print('YES')
    elif s[2] == s[0] == s[4]:
        print('YES')
    elif s[2] == s[1] == s[5]:
        print('YES')
    elif s[2] == s[1] == s[4]:
        print('YES')
    elif s[3] == s[0] == s[5]:
        print('YES')
    elif s[3] == s[0] == s[4]:
        print('YES')
    elif s[3] == s[1] == s[5]:
        print('YES')
    elif s[3] == s[1] == s[4]:
        print('YES')
    else:
        print('NO')
