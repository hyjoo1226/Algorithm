A, B = map(int, input().split())

for i in range(1, 10):
    for j in range(B, A - 1, -1):
        if j % 2 == 0:
            if j == A:
                print(f'{j} * {i} = {i * j}')
            else:
                print(f'{j} * {i} = {i * j}', end = ' / ')