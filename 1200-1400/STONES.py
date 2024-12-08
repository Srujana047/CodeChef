T=int(input())
for _ in range(T):
    j = input()
    s = input()
    count = 0
    maxi = min(len(j),len(s))
    for i in s:
        if i in j:
            count+=1
    print(count)
