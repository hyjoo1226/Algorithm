from collections import deque

di = [-1, 0, 0, 1]  #델타좌표 상좌우하
dj = [0, -1, 1, 0]
N = int(input())    #NxN 공간
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            start = [i, j, 2, 2, 0] # 시작좌표 i, j, 크기 2, 남은 먹이 2, 레벨 0
            arr[i][j] = 0   #상어 있던 곳 0
visited = [[0] * N for _ in range(N)]   #방문 기록
q = deque([])   #큐 생성
q.append(start)
t = 0   #시간

while q:
    current = q.popleft()   #현재 위치
    visited[current[0]][current[1]] = 1
    token = 0   #전부 0이면 종료
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0 and arr[i][j] < current[2]: #먹을게 있으면 토큰 1
                token = 1
                break
        if token == 1:
            break

    if arr[current[0]][current[1]] != 0 and current[2] > arr[current[0]][current[1]]:    #먹을 수 있는 물고기가 있으면
        current[3] -= 1 #남은 먹이 -1
        arr[current[0]][current[1]] = 0 #먹이 먹었으므로 물고기 x
        visited = [[0] * N for _ in range(N)]  # 방문 기록 초기화
        q = deque()   #큐 초기화
        t += current[4] #레벨만큼 시간 추가
        current[4] = 0  #레벨 초기화
        if current[3] == 0: #남은 먹이 없으면 크기 커지고, 남은 먹이 개수 초기화
            current[2] += 1
            current[3] = current[2]

    if token == 0:  #물고기 없으면 while문 종료
        break

    for k in range(4):
        ni = current[0] + di[k]
        nj = current[1] + dj[k]
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and current[2] >= arr[ni][nj]:    #인덱스 범위 내에서 방문안했고 이동할 수 있는 곳이면
            q.append([ni, nj, current[2], current[3], current[4] + 1])
print(t)
