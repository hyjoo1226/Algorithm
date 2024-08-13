T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())    #NxM 행렬 입력
    arr = [[0] * M for _ in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    max_sum = 0 #꽃가루의 합 최대값
    for i in range(N):
        for j in range(M):
            sum = arr[i][j] #상하좌우 중앙합
            temp = arr[i][j]
            for idx in range(1, temp + 1):
                di = [-idx, idx, 0, 0]  # 상하좌우 델타좌표
                dj = [0, 0, -idx, idx]
                for k in range(4):
                    if 0 <= i + di[k] < N and 0 <= j + dj[k] < M:   #인덱스범위내에서
                        sum += arr[i + di[k]][j + dj[k]]
            if max_sum < sum:
                max_sum = sum

    print(f'#{tc} {max_sum}')
