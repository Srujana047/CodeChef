T = int(input())
for i in range(T):
    d,c = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    x = sum(a)
    y = sum(b)
    
    day1,day2,wc=0,0,0
    woc = x+d+y+d
    
    if x>=150 and y>=150:
        wc = x+y+c
    elif x>=150 and y<=150:
        day1 = x+c
        day2 = y+d
        wc = day1+day2
    elif y>=150 and x<=150:
        day1 = x+d
        day2 = y+c
        wc = day1+day2
    else:
        wc = x+d+y+d
    
    if wc<woc:
        print("YES")
    else:
        print("NO")
