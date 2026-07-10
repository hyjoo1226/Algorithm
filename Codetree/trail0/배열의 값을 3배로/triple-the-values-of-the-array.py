arr = []
for _ in range(3):
    arr.append(list(map(int, input().split())))

for i in range(3):
    for j in range(3):
        print(arr[i][j] * 3, end = ' ')
    print()