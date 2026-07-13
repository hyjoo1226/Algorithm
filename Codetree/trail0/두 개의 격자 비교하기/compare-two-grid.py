N, M = map(int, input().split())

arr1 = []
arr2 = []

for _ in range(N):
    arr1.append(input().split())

for _ in range(N):
    arr2.append(input().split())

for i in range(N):
    for j in range(M):
        if arr1[i][j] == arr2[i][j]:
            print("0", end = ' ')
        else:
            print("1", end = ' ')
    print()
