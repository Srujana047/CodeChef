T=int(input())
for _ in range(T):
    s = input().split(" ")
    l = len(s)
    if l==1:
        s = str(s[0])
        print(s[:1].upper() + s[1:].lower())
    elif l==2:
         s1 = str(s[0])
         s2 = str(s[1])
         print(s1[:1].upper() + ". " + s2[:1].upper() + s2[1:].lower())
    else:
         s1 = str(s[0])
         s2 = str(s[1])
         s3 = str(s[2])
         print(s1[:1].upper() + ". " + s2[:1].upper() + ". " + s3[:1].upper() + s3[1:].lower())   
