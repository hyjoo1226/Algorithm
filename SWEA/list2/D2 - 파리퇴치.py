T = int(input())

for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))

    arr = [0] * N   # NxN 행렬 초기화
    for i in range(N): # 행렬에 주어진 값 입력
        arr[i] = list(map(int, input().split()))
    
    max_sum = 0 #파리 죽인 최댓값
    for i in range(0, N - M + 1):   #인덱스 초과안하는 범위에서 파리채가 arr 순회
        for j in range(0, N - M + 1):
            num_sum = 0
            for a in range(i, i + M):   #파리채 범위 합
                for b in range(j, j + M):
                    num_sum += arr[a][b]

            if max_sum < num_sum:
                max_sum = num_sum
    
    print(f'#{test_case} {max_sum}')