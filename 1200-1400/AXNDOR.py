T = int(input())
for i in range(T):
    n = int(input())
    if n % 4 == 0 :
        print(n+3)
    elif n%4==2 or n%4==3:
        print(3)
    else:
        print(n)
