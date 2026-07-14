N = int(input())

for i in range(1, N + 1):
    ss = str(i)
    checker = 0
    if i % 3 == 0:
        print(0, end = ' ')
        checker = 1
    else:
        for s in ss:
            if s in ['3', '6', '9']:
                print(0, end = ' ')
                checker = 1
                break
    if checker == 0:
        print(i, end = ' ')