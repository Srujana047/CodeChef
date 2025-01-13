t = int(input())
for _ in range(t):
    m, w = input().split()
    i, j = 0, 0 
    while i < len(m) and j < len(w):
        if m[i] == w[j]:
            i += 1
        j += 1
    mofw = (i == len(m))
    i, j = 0, 0 
    while i < len(w) and j < len(m):
        if w[i] == m[j]:
            i += 1
        j += 1
    wofm = (i == len(w))
    if mofw or wofm:
        print("YES")
    else:
        print("NO")
