T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    memo = []   #메모이제이션
    for i in range(N):
        memo.append([1] * (i + 1))

    for i in range(2, N):   #N = 1, 2인 경우 모두 1이므로
        for j in range(1, i):   #양 끝은 1이므로
            memo[i][j] = memo[i - 1][j - 1] + memo[i - 1][j]    #파스칼삼각형 패턴

    print(f'#{tc}')
    for i in range(N):
        print(*memo[i])