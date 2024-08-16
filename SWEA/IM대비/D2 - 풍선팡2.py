T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0] * M for _ in range(N)]   #NxM배열 입력
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    di = [-1, 1, 0, 0]  #상하좌우 델타좌표
    dj = [0, 0, -1, 1]
    max_sum = 0 #최대 개수
    for i in range(N):
        for j in range(M):
            sum = arr[i][j] #꽃가루 합
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M: #인덱스 범위내에서
                    sum += arr[ni][nj]  #상하좌우 더하기
            if max_sum < sum:
                max_sum = sum

    print(f'#{tc} {max_sum}')