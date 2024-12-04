T = int(input())
for i in range(T):
    n = int(input())
    s = list(map(str,input().split()))
    if n == 1:
        if s[0] == 'cookie':
            print('NO')
        else:
            print('YES')
        
    else:
        for i in range(n-1):
            if (s[i]=='cookie' and s[i+1] == 'cookie') or s[-1] == 'cookie':
                print("NO")
                break
        else:
            print("YES")
