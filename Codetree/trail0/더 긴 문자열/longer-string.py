a, b = input().split()

if len(a) == len(b):
    print('same')
else:
    if len(a) > len(b):
        print(a, len(a))
    else:
        print(b, len(b))