N = int(input())

mat = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(i + 1):
        if i % 2 == 0:
            mat[i][0] = 1
        else:
            mat[i][j] = 1


for i in range(N):
    for j in range(N):
        if mat[j][i] == 1:
            print('*', end = ' ')
        elif mat[j][i] == 0:
            print(' ', end = ' ')
    print()