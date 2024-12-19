T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    
    count5 = 0
    count10 = 0
    can_serve = True
    
    for coin in a:
        if coin == 5:
            count5 += 1
        elif coin == 10:
            if count5 > 0:
                count5 -= 1
                count10 += 1
            else:
                can_serve = False
                break
        elif coin == 15:
            if count10 > 0:
                count10 -= 1
            elif count5 >= 2:
                count5 -= 2
            else:
                can_serve = False
                break
    
    print("YES" if can_serve else "NO")
