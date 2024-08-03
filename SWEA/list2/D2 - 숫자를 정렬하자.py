#버블정렬
def bubble_sort(num_lst, N):
    for i in range(N - 1):
        for j in range(i, N - 1):
            if num_lst[j] > num_lst[j + 1]:
                num_lst[j], num_lst[j + 1] = num_lst[j + 1], num_lst[j]
    return num_lst

#선택정렬
def selection_sort(num_lst, N):
    for i in range(N - 1):
        min_idx = i
        for j in range(i + 1, N):
            if num_lst[min_idx] > num_lst[j]:
                min_idx = j
        num_lst[i], num_lst[min_idx] = num_lst[min_idx], num_lst[i]

    return num_lst

#카운팅정렬
def counting_sort(num_lst, N):
    max_num = max(num_lst)
    temp = [0] * N
    counts = [0] * (max_num + 1)
    for item in num_lst:
        counts[item] += 1

    for i in range(1, max_num + 1):
        counts[i] += counts[i - 1]

    for i in range(N - 1, -1, -1):
        counts[num_lst[i]] -= 1
        temp[counts[num_lst[i]]] = num_lst[i]

    return temp

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())    #숫자의 개수
    num_lst = list(map(int, input().split()))   #숫자 리스트

    # result = bubble_sort(num_lst, N)
    # result = selection_sort(num_lst, N)
    result = counting_sort(num_lst, N)
    print(f'#{test_case}', *result)