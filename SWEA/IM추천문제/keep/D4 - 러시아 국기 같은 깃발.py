T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())    #NxM 깃발
    flag = [0] * N
    for i in range(N):
        flag[i] = input()   #기존 깃발 입력

    W_lst = []
    B_lst = []
    R_lst = []
    for i in range(N):  #각 색깔로 칠해야 하는 횟수
        W = 0
        B = 0
        R = 0
        for j in range(M):
            if flag[i][j] == 'W':
                B += 1
                R += 1
            elif flag[i][j] == 'B':
                W += 1
                R += 1
            else:
                W += 1
                B += 1
        W_lst.append(W)
        B_lst.append(B)
        R_lst.append(R)

    color = W_lst[0] + R_lst[-1]   #색칠횟수(첫줄 White, 마지막줄 Red)
    max_temp = 2500
    for i in range(1, N - 1):  #중간줄(Blue 위치 정해서), W_lst[: i] B_lst[i : j] R_lst[j :]
        for j in range(i, N - 1):
            check = 0  # Blue 하나라도 있으면 1
            temp = 0  # 임시저장
            if i != 1:  #예외: 중간줄 W없을때
                for k in range(i):
                    temp += W_lst[k]
            if i == N - 2:  #예외: 중간줄 R없을때
                temp += B_lst[k + 1]
                check = 1
                if max_temp > temp and check == 1:  # Blue줄 있을 때 최솟값
                    max_temp = temp
                break
            for k in range(i, j):
                temp += B_lst[k]
                check = 1
            for k in range(j, N - 1):
                temp += R_lst[k]
            if max_temp > temp and check == 1:  #Blue줄 있을 때 최솟값
                max_temp = temp

    color += max_temp   #중간줄 색칠횟수 더하기
    print(f'#{tc} {color}')
