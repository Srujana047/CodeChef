T = int(input())
for _ in range(T):
    n = int(input())
    total = 0.0
    for _ in range(n):
        price, quantity, discount = map(int, input().split())
        ip = price * (1 + discount / 100)
        fp = ip * (1 - discount / 100)
        diff = price - fp
        total += diff * quantity
    print(f"{total:.6f}")
