T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    i = 0
    c = 0
    co = list()
    while i < n:
        if i == n-1:
            co.append(c + 1)
        elif a[i] == a[i+1]:
            c += 1
        else:
            co.append(c + 1)
            c = 0
        i += 1
    numbers = list()
    counter = list()
    for j in a:
        if j in numbers:
            next
        else:
            numbers.append(j)
            counter.append(a.count(j))
    if co != counter:
        print("NO")
    else:
        corr = True
        for k in counter:
            if counter.count(k) > 1:
                print("NO")
                corr = False
                break
        if corr:
            print("YES")
    
