T = int(input())
for i in range(T):
    a = input()
    b = input()
    count = 0
    if((a[0]=='b'or b[0]=='b')and(a[1]=='o'or b[1]=='o') and (a[2]=='b'or b[2]=='b')):
        print("yes")
    elif((a[0]=='o'or b[0]=='o')and(a[1]=='b'or b[1]=='b') and (a[2]=='b'or b[2]=='b')):
        print("yes")
    elif((a[0]=='b'or b[0]=='b')and(a[1]=='b'or b[1]=='b') and (a[2]=='o'or b[2]=='o')):
        print("yes")
    else:
        print("no")
