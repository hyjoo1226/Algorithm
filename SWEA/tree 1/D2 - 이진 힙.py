def enq(n): #최소힙
    global last
    last += 1
    h[last] = n
    c = last
    p = c // 2
    while p >= 1 and h[p] > h[c]:
        h[p], h[c] = h[c], h[p]
        c = p
        p = c//2

T = int(input())
for tc in range(1, T + 1):
    N = int(input())    #N개의 자연수
    N_lst = list(map(int, input().split())) #입력 순서

    h = [0] * (N + 1)   #힙
    last = 0    #힙의 마지막 노드 번호
    for item in N_lst:  #최소힙 만들기
        enq(item)

    num_sum = 0
    while N != 1:   #합구하기
        N = N // 2
        num_sum += h[N]
    
    print(f'#{tc} {num_sum}')