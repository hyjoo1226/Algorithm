mat = []
for _ in range(4):
    row_data = list(map(int, input().split()))
    mat.append(row_data)

total = 0
for i in range(4):
    for j in range(4):
        if j <= i:
            total += mat[i][j]

print(total)