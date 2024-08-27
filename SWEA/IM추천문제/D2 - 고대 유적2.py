T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # NxM배열
    arr = [[0] * M for _ in range(N)]

    for i in range(N):
        arr[i] = list(map(int, input().split()))

        count = 0   #가장 긴 구조물
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 1:  # 구조물발견
                    k = 0
                    while j + k < M and arr[i][j + k] == 1:  # 인덱스범위내에서
                        k += 1
                    if k > 1 and count < k: #구조물 길이
                        count = k

                    k = 0
                    while i + k < N and arr[i + k][j] == 1:
                        k += 1
                    if k > 1 and count < k:
                        count = k

    print(f'#{tc} {count}')