T = int(input())
for i in range(T):
    n = int(input())
    l =[]
    for i in range(n):
        s = input()
        s = set(list(s))
        l.append(s)
    x = l[0]
    for i in l[1::]:
        x = x.intersection(i)
    print(len(x))
