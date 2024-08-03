T = int(input())

for test_case in range(1, T + 1):
#   (0,0) ~ (0, N - 1) ~ (N - 1, N - 1) ~ (N - 1, 0)
#   ~ (1, 0) ~ (1, N - 2) ~ (N - 2, N - 2) ~ (N - 2, 1)
#   ~ (2, 0)
    N = int(input())
    arr = [[0] * N for _ in range(N)]   #NxN배열 0으로 초기화
    number = 0  #시작 값

    i = 0   #이동하는 좌표 위치
    j = 0
    di = [0, 1, 0, -1]    #우 - 하 - 좌 - 상 델타좌표와 델타인덱스
    dj = [1, 0, -1, 0]
    d_index = 0
    while number < N ** 2:
        number += 1
        arr[i][j] = number  # 이동한 좌표에 1증가한 number 대입
        #끝 모서리거나 다음 좌표가 이미 지나간 곳이면 델타좌표 다음 인덱스로 바꿔준다
        if (i == 0 and j == N - 1) or (i == N - 1 and j == N - 1) or \
                    (i == N - 1 and j == 0) or (arr[i + di[d_index]][j + dj[d_index]] != 0):
            d_index = (d_index + 1) % 4

        i += di[d_index] #좌표 이동
        j += dj[d_index]

    print(f'#{test_case}')
    for k in range(N):
        print(*arr[k])