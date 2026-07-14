a, b, c = map(int, input().split())

if a <= b:
    if a <= c:
        print(a)
    else:
        print(c)

elif a <= c:
    if a <= b:
        print(a)
    else:
        print(b)

elif b <= a:
    if b <= c:
        print(b)
    else:
        print(c)
    
elif b <= c:
    if b <= a:
        print(b)
    else:
        print(a)

elif c <= a:
    if c <= b:
        print(c)
    else:
        print(b)

else:
    if c <= a:
        print(c)
    else:
        print(a) 