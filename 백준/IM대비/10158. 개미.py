w, h = map(int, input().split())    #w x h 격자공간
x, y = map(int, input().split())    #x, y 좌표
t = int(input())    #개미가 움직일 시간 t
di = [1, 1, -1, -1] #대각 델타좌표 1, 11, 7, 5시 방향으로 진행
dj = [1, -1, -1, 1]
idx = 0
current = [y, x, 1, 1]    #현재 개미 위치, 진행방향(i증가면 1, i감소면 -1 / j~)
for k in range(t):  #t번 이동
    if current[0] == 0 and current[1] == 0: #모서리
        idx = 0
        current[2] = 1
        current[3] = 1
    elif current[0] == h and current[1] == w:
        idx = 2
        current[2] = -1
        current[3] = -1
    elif current[0] == 0 and current[1] == w:
        idx = 1
        current[2] = 1
        current[3] = -1
    elif current[0] == h and current[1] == 0:
        idx = 3
        current[2] = -1
        current[3] = 1
    elif current[2] == 1 and current[1] == w: #1시방향 이동 중 오른쪽 벽 충돌
        idx = 1
        current[3] = -1
    elif current[2] == -1 and current[1] == w:  #5시방향 이동 중 오른쪽 벽 충돌
        idx = 2
        current[3] = -1
    elif current[2] == 1 and current[1] == 0:   #11시방향 이동 중 왼쪽 벽 충돌
        idx = 0
        current[3] = 1
    elif current[2] == -1 and current[1] == 0:  #7시방향 이동 중 왼쪽 벽 충돌
        idx = 3
        current[3] = 1
    elif current[3] == 1 and current[0] == h:   #1시방향 이동 중 위쪽 벽 충돌
        idx = 3
        current[2] = -1
    elif current[3] == -1 and current[0] == h:  #11시방향 이동 중 위쪽 벽 충돌
        idx = 2
        current[2] = -1
    elif current[3] == 1 and current[0] == 0:   #5시방향 이동 중 아래쪽 벽 충돌
        idx = 0
        current[2] = 1
    elif current[3] == -1 and current[0] == 0:  #7시방향 이동 중 아래쪽 벽 충돌
        idx = 1
        current[2] = 1
    current[0] += di[idx]   #개미 이동
    current[1] += dj[idx]

print(current[1], current[0])