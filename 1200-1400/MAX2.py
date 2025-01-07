n = int(input())
b = input()
a = b[::-1]
count=0;
for i in a:
    if i == '0':
        count += 1
    elif i == '1':
        break
print(count)
