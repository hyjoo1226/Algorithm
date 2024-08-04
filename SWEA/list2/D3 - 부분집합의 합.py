T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())    #원소의 수 N, 부분집합의 합 K

    for i in range(1 << N): # 이진수 00...01을 왼쪽으로 N비트 이동 -> 10...00 -> 10진수로 2의 N제곱과 같은 값
        subset_len = 1  #부분집합의 길이
        subset_sum = 0  #부분집합의 합

        for j in range(N):
            if i & (1 << j): #만약 i의 j번 비트가 1인 경우
