T = int(input())
for tc in range(1, T + 1):
    N = int(input())    #NxN배열
    arr = [[0] * N for _ in range(N)]
    temp = [[0] * N for _ in range(N)]
    for i in range(N):
        arr[i] = list(input().split())

    for i in range(N):
        for j in range(N):
            if i == 0:
                temp[i][j] =