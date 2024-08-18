T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())    #회문의 길이 M
    arr = [[0] * N for _ in range(N)]   #NxN행렬 초기화 후 입력값 받기
    for i in range(N):
        arr[i] = input()

    result = ''
    i_token = 0
    j_token = 0
    for i in range(N):
        for j in range(0, N - M + 1):
            j_token = 0
            for k in range(M):
                if arr[i][j + k] != arr[i][j + M - k - 1]:
                    j_token = 1
            if j_token == 0:
                result = arr[i][j : j + M]
                break
        if j_token == 0:
            break

    for i in range(0, N - M + 1):
        for j in range(N):
            i_token = 0
            for k in range(M):
                if arr[i + k][j] != arr[i + M - k - 1][j]:
                    i_token = 1
            if i_token == 0:
                for k in range(M):
                    result += arr[i + k][j]
                break
        if i_token == 0:
            break

    print(f'#{tc} {result}')