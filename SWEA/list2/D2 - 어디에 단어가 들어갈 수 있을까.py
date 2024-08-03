import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, K = list(map(int, input().split()))  #NxN배열, 단어의 길이 K

    arr = [[0] * N for _ in range(N)]   #NxN배열 0으로 초기화 후 케이스 값 대입
    for i in range(N):
        temp = list(map(int, input().split()))
        for j in range(N):
            arr[i][j] = temp[j]

    result = 0
    for i in range(N):
        count_width = 0
        count_length = 0
        for j in range(N):
            if arr[i][j] == 1:   #가로로 배열 순회하면서 1인 경우(빈칸인 경우) count 1 증가
                count_width += 1
            else:
                if count_width == K:  #0을 만났을 때 count가 단어의 길이(K)와 같으면 result 1 증가
                    result += 1
                count_width = 0   #0을 만났으므로 count 0으로 초기화

            if arr[j][i] == 1:  #세로인 경우
                count_length += 1
            else:
                if count_length == K:
                    result += 1
                count_length = 0

        if count_width == K:  #마지막 인덱스가 1인 경우
            result += 1
        if count_length == K:
            result += 1

    print(f'#{test_case} {result}')