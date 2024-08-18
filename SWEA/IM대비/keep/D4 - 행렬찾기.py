T = int(input())
for tc in range(1, T + 1):
    n = int(input())    #nxn 행렬
    arr = [[] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]   #방문x면 0, o면 1
    for i in range(n):
        arr[i] = list(map(int, input().split()))

    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:  #화학물질담겼으면

