T = int(input())
for i in range(T):
    n=int(input())
    x=len(bin(n)[2:])-1
    print(n-x-1)
