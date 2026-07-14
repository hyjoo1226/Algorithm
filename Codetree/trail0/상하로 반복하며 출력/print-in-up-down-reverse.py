N = int(input())

mat = []
num = 0

for i in range(1, N + 1):
    row_data = []
    for j in range(1, N + 1):
        if j % 2 != 0:
            row_data.append(1 + num)
        else:
            row_data.append(N - num)
    mat.append(row_data)
    num += 1

for i in range(N):
    for j in range(N):
        print(mat[i][j], end='')
    print()