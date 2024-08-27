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
        arr[2][1] = 'B'
        arr[2][2] = 'W'
    elif N == 6:
        arr = [[0] * 6 for _ in range(6)]
        arr[2][2] = 'W'
        arr[2][3] = 'B'
        arr[3][2] = 'B'
        arr[3][3] = 'W'
    else:
        arr = [[0] * 8 for _ in range(8)]
        arr[3][3] = 'W'
        arr[3][4] = 'B'
        arr[4][3] = 'B'
        arr[4][4] = 'W'
    i = 0
    while i < M:    #게임 시작
        i += 1
        X, Y, color = map(int, input().split()) #XY좌표, 돌색깔
        if color == 1:  #흑돌
            arr[Y - 1][X - 1] = 'B'
            stack = []  #현재 좌표와 진행 방향 담긴 스택
            change = [] #돌 색깔 바꿀 좌표 리스트
            for k in range(8):  #델타좌표 W스캔. W있으면 해당 좌표 스택에 넣기
                if 0 <= Y - 1 + di[k] < N and 0 <= X - 1 + dj[k] < N:   #인덱스 범위 내에서
                    if arr[Y - 1 + di[k]][X - 1 + dj[k]] == 'W':    #백돌이 델타좌표에 있으면 스택에 좌표 추가
                        stack.append([Y - 1 + di[k], X - 1 + dj[k], k])
                        # change.append([Y - 1 + di[k], X - 1 + dj[k]])
            while stack:    #스택빌때까지
                current = stack.pop()   #좌표 한개 꺼내기
                if 1 <= current[0] + di[current[2]] < N and 1 <= current[1] + dj[current[2]] < N:
                    if arr[current[0] + di[current[2]]][current[1] + dj[current[2]]] == 'W':    #또 W면 change(바꿀 리스트)에 추가
                        if current[0] + di[current[2]] == 1 or current[0] + di[current[2]] == N - 1 or current[1] + dj[current[2]] == 1 or current[1] + dj[current[2]] == N - 1:
                            change = [] #그대로 인덱스가 끝난 경우
                        else:
                            change.append(current)  #같은 방향으로 계속 진행
                            stack.append([current[0] + di[current[2]], current[1] + di[current[2]], current[2]])
                    elif arr[current[0] + di[current[2]]][current[1] + dj[current[2]]] == 'B':  #B만나면 change에 들어있던 값 바꾸기
                        change.append(current)
                        for p in range(len(change)):
                            arr[change[p][0]][change[p][1]] = 'B'
                    else:   #돌이 없다면 change 초기화
                        change = []

        else:   #백돌
            arr[Y - 1][X - 1] = 'W'
            stack = []
            change = []
            for k in range(8):
                if 0 <= Y - 1 + di[k] < N and 0 <= X - 1 + dj[k] < N:
                    if arr[Y - 1 + di[k]][X - 1 + dj[k]] == 'B':
                        stack.append([Y - 1 + di[k], X - 1 + dj[k], k])
                        # change.append([Y - 1 + di[k], X - 1 + dj[k]])
            while stack:
                current = stack.pop()
                if 1 <= current[0] + di[current[2]] < N and 1 <= current[1] + dj[current[2]] < N:
                    if arr[current[0] + di[current[2]]][current[1] + dj[current[2]]] == 'B':
                        if current[0] + di[current[2]] == 1 or current[0] + di[current[2]] == N - 1 or current[1] + dj[current[2]] == 1 or current[1] + dj[current[2]] == N - 1:
                            change = []
                        else:
                            change.append(current)
                            stack.append([current[0] + di[current[2]], current[1] + di[current[2]], current[2]])
                    elif arr[current[0] + di[current[2]]][current[1] + dj[current[2]]] == 'W':
                        change.append(current)
                        for p in range(len(change)):
                            arr[change[p][0]][change[p][1]] = 'W'
                    else:  # 돌이 없다면 change 초기화
                        change = []
        print(i, M)

    pprint(arr)