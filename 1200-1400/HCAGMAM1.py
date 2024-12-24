T = int(input())
for _ in range(T):
    x,y = map(int,input().split())
    s = input()
    a = s.count('1')
    a*=x
    count = 0
    maxi = 0
    for i in s:
        if i == '1':
            count+=1
        else:
            maxi = max(maxi,count)
            count = 0
    maxi = max(maxi,count)
    maxi *= y
    print(maxi+a)
