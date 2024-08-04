T = int(input())

for tc in range(1, T + 1):
    N = int(input())    #정수의 개수
    num_lst = list(map(int, input().split()))   #정수값 리스트

    for i in range(N - 1):  #선택정렬
        min_idx = i
        for j in range(i + 1, N):
            if num_lst[min_idx] > num_lst[j]:
                min_idx = j
        num_lst[i], num_lst[min_idx] = num_lst[min_idx], num_lst[i]

    print(f'#{tc}', end = ' ')
    for i in range(5):  #큰값 작은값 순서대로 출력
        print(num_lst[N - i - 1], num_lst[i], end = ' ')
    print()