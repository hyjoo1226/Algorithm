T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[1] * N for _ in range(N)]   #NxN 오목판 입력
    for i in range(N):
        arr[i] = input()

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':    #내 위치에 돌이 있다면
                for a in range(1, 5):   #자기 위치 + 최대 4까지
                    di = [-a, a, 0, 0, -a, a, -a, a]  # 상하,좌우,대각,반대각 델타좌표
                    dj = [0, 0, -a, a, a, -a, -a, a]

                for b in range(8):
                    arr[i + di[b]][j + dj[b]]
