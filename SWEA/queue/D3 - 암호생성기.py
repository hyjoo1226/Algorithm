for tc in range(1, 11):
    n = int(input())    #tc 번호
    num_lst = list(map(int, input().split()))   #8개의 숫자 리스트 <- 큐로 사용
    front = 0
    rear = 7
    while num_lst[rear] > 0: #숫자 리스트의 마지막 값이 0보다 큰 동안 반복
        for i in range(1, 6):  # 한 사이클 5번 값 감소(1, 2, 3, 4, 5)
            temp = num_lst[front] - i   #감소시킨 값 temp에 임시저장
            front = (front + 1) % 8
            rear = (rear + 1) % 8
            num_lst[rear] = temp    #temp값 rear에 추가
            if num_lst[rear] <= 0:
                break

    print(f'#{tc}', end = ' ')    #출력
    for i in range(rear + 1, 8):
        print(num_lst[i], end = ' ')
    for i in range(0, rear):
        print(num_lst[i], end = ' ')
    print('0')