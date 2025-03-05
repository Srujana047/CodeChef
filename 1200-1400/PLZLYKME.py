T = int(input())  
for _ in range(T):
    l,d,s,c = map(int, input().split())  
    d1 = s  
    for i in range(1, d):  
        d1 += d1 * c  
        if d1 >= l:  
            print("ALIVE AND KICKING")
            break
    else:  
        if d1 >= l:
            print("ALIVE AND KICKING")
        else:
            print("DEAD AND ROTTING")
