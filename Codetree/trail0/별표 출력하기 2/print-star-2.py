N = int(input())

for i in range(N):
    for j in range(N - i):
        print('*', end=' ')
    for k in range(i):
        print(' ', end=' ')
    print()