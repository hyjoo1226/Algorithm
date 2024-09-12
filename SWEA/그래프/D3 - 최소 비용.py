from collections import deque

def BFS(start):
    global di, dj, min_use
    q = deque([start])   #큐
    visited = [[0] * N for _ in range(N)]  # 방문 기록
    while q:
        current = q.popleft()   #현재 좌표
        visited[current[0]][current[1]] = 1  # 방문 체크
        for k in range(4):
            ni = current[0] + di[k]
            nj = current[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:    #인덱스 범위 내에서 방문 안한 곳이면
                q.append([ni, nj])  #큐에 추가
                if arr[current[0]][current[1]] >= arr[ni][nj]:  #더 낮거나 같은 높이면
                    visited[ni][nj] += 1
                else:   #더 높으면
                    visited[ni][nj] += arr[ni][nj] - arr[current[0]][current[1]] + 1



di = [1, 0, -1, 0] #상하좌우 델타좌표
dj = [0, 1, 0, -1]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]   #NxN 배열 입력
    min_use = 10000000 #최소 연료 소비량
    BFS([0, 0])   #시작 좌표
    print(f'#{tc} {min_use}')