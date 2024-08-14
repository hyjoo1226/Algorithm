from pprint import pprint
di = [1, -1, 0, 0, 1, -1, 1, -1]    #상하좌우대각 델타좌표
dj = [0, 0, 1, -1, -1, 1, 1, -1]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())    #한 변의 길이N, 돌을 놓는 횟수 M

    if N == 4:  #오셀로판 초기세팅
        arr = [[0] * 4 for _ in range(4)]
        arr[1][1] = 'W'
        arr[1][2] = 'B'
        arr[2][1] = 'W'
        arr[2][2] = 'B'
    elif N == 6:
        arr = [[0] * 6 for _ in range(6)]
        arr[2][2] = 'W'
        arr[2][3] = 'B'
        arr[3][2] = 'W'
        arr[3][3] = 'B'
    else:
        arr = [[0] * 8 for _ in range(8)]
        arr[3][3] = 'W'
        arr[3][4] = 'B'
        arr[4][3] = 'W'
        arr[4][4] = 'B'

    i = 0
    while i < M:    #게임 시작
        i += 1
        X, Y, color = map(int, input().split()) #XY좌표, 돌색깔
        if color == 1:  #흑돌
            arr[Y - 1][X - 1] = 'B'
            xy_lst = []
            for k in range(8):  #델타좌표 W스캔. W있으면 해당 좌표 기록
                if arr[Y - 1 + di[k]][X - 1 + dj[k]] == 'W':
                    xy_lst.append([Y - 1 + di[k], X - 1 + dj[k]])

        else:   #백돌
            arr[Y - 1][X - 1] = 'W'

        print(arr)