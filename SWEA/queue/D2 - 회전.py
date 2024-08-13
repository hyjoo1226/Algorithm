T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())    #N개의 숫자로 이루어진 수열, 작업횟수 M
    num_lst = list(map(int, input().split()))   #숫자 리스트 <- 원형큐
    front = 0
    rear = N - 1

    for i in range(M):  #맨 앞의 숫자를 맨 뒤로 보내는 작업 M번
        temp = num_lst[front]    #맨 앞 숫자(front) 임시저장
        front = (front + 1) % N
        rear = (rear + 1) % N
        num_lst[rear] = temp    #맨 뒤에(rear) 넣어주기

    print(f'#{tc} {num_lst[front]}')