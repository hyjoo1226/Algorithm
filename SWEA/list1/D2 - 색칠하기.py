T = int(input())

for test_case in range(1, T + 1):
    N = int(input())    #색칠영역 개수

    arr = [[0] * 10 for _ in range(10)] #10x10 격자 생성

    for k in range(N):
        space = list(map(int, input().split()))

        for i in range(10): #10x10격자 순회하면서
            for j in range(10):
                if space[-1] == 1:  #red 영역인 경우 해당 값 1 증가
                    if i > space[0] - 1 and j > space[1] - 1 and \
                    i <= space[2] and j <= space[3]:
                        arr[i][j] += 1
                else:   #blue 영역인 경우 해당 값 2 증가
                    if i > space[0] - 1 and j > space[1] - 1 and \
                    i <= space[2] and j <= space[3]:
                        arr[i][j] += 2
        
        count = 0
        for i in range(10): #같은 색 영역은 겹치지 않으므로 값이 3인 영역이 보라색
            for j in range(10):
                if arr[i][j] == 3:
                    count += 1
    
    print(f'#{test_case} {count}')