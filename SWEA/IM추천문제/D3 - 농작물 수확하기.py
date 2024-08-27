T = int(input())
for tc in range(1, T + 1):
    N = int(input())    #NxN농장
    farm = [[0] * N for _ in range(N)]
    for i in range(N):
        temp = input()
        for j in range(N):
            farm[i][j] = int(temp[j])

    income = 0  #수익
    for i in range(N):
        for j in range(N):
            if i <= N // 2: #행의 절반
                if N // 2 - 1 - i < j < N // 2 + 1 + i:
                    income += farm[i][j]
            else:   #나머지 행
                if i - N // 2 - 1 < j < N - i + N // 2:
                    income += farm[i][j]

    print(f'#{tc} {income}')