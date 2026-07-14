a = 0
for _ in range(3):
    c, t = input().split()
    if c == 'Y' and int(t) >= 37:
        a += 1

if a >= 2:
    print('E')
else:
    print('N')