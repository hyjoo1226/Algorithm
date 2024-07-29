def num_sum(a_lst, M, i):
    temp = 0

    for j in range(M):
        temp += a_lst[i]
        i += 1

    return temp

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    a_lst = list(map(int, input().split()))

    num_max = num_sum(a_lst, M, 0)
    num_min = num_sum(a_lst, M, 0)

    for i in range(N - M + 1):
        num_result = num_sum(a_lst, M, i)

        if num_max < num_result:
            num_max = num_result
        if num_min > num_result:
            num_min = num_result

    print(f'#{test_case} {num_max - num_min}')