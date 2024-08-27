import sys
sys.stdin = open('input (1).txt')

for tc in range(1, 11):
    num = int(input())
    arr = [[0] * 100 for _ in range(100)]
    for i in range(100):
        arr[i] = list(map(int, input().split()))    #입력값받기

    trans_arr = list(map(list, zip(*arr)))  #행 열 뒤집기

    count = 0   #교착상태
    for i in range(100):
        N_token = 0
        for j in range(100):
            if trans_arr[i][j] == 1:    #N이 위에 있을때
                N_token = 1
            elif trans_arr[i][j] == 2:  #S가 나타나면 교착상태 +1
                if N_token == 1:
                    count += 1
                    N_token = 0
    print(f'#{tc} {count}')