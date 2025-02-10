T = int(input())
for i in range (T):
    a = list(map(int, input().split()))
    a.sort()
    if (a[1] != a[2] or (a[1] == a[2]and a[0] != a[1]and a[2] != a[3])):
        print('2')
    elif (a[0] == a[3]):
        print('0')
    else:
        print('1')
