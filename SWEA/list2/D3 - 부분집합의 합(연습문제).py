T = int(input())

for test_case in range(1, T + 1):
    num_lst = list(map(int, input().split()))   #입력된 정수 10개 들어있는 리스트

    for i in range(9):  #선택정렬
        min_idx = i
        for j in range(i + 1, 10):
            if num_lst[min_idx] > num_lst[j]:
                min_idx = j
        num_lst[i], num_lst[min_idx] = num_lst[min_idx], num_lst[i]

    result = 0  #부분집합의 합이 0이 되는 것이 있으면 1, 없으면 0
    minus = 0   #음수가 있으면 1, 없으면 0
    for item in num_lst:
        if item == 0:
            result = 1
            break
        if item < 0:
            minus = 1

    if result == 1: #0이 있으면 result 1 출력
        print(f'#{test_case} {result}')
    elif minus == 0 and result == 0:  #모두 양수면 result 0 출력
        print(f'#{test_case} {result}')
    else:
        num_sum = 0 #부분집합의 합
        for i in range(10):
            for j in range(i0)

