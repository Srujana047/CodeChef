T = int(input())
for i in range(T):
    n = int(input())
    a = input()
    b = input()
    count = 0
    evy = 0
    for i in range(n):
        if a[i] == '1' and b[i] == '1':
            count +=1
        elif a[i] == '10' and b[i] == '10':
            evy+=1
    if count%2!=0:
        print("yes")
    else:
        if evy>=1:
            print("yes")
        else:
            print("no")
