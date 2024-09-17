T = int(input())
for tc in range(1, T + 1):
    N = int(input())    #NxN
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]   #방문할때 상 좌 중 작은 값을 더해주기
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:   #시작값
                visited[i][j] = arr[i][j]
            elif i == 0:    #첫줄
                visited[i][j] = visited[i][j - 1] + arr[i][j]
                visited[j][i] = visited[j - 1][i] + arr[j][i]
            elif j != 0:
                visited[i][j] = min(visited[i - 1][j], visited[i][j - 1]) + arr[i][j]
    print(f'#{tc} {visited[N - 1][N - 1]}')
