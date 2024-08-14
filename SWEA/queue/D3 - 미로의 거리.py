##DFS 재귀 방법도 있음

#BFS
T = int(input())
for tc in range(1, T + 1):
    N = int(input())    #N개의 줄
    arr = [[0] * N for _ in range(N)] #NxN배열 생성
    visited = [[0] * N for _ in range(N)] #방문장소 기록(방문하면 기존 좌표에 1씩 추가,아니면0)
    q = []  #큐 생성
    start = [-1, -1]  #시작지점
    di = [-1, 1, 0, 0]  #델타좌표 상하좌우
    dj = [0, 0, -1, 1]
    result = 0  #최종결과
    token = 0   #반복문 탈출위한 토큰
    for i in range(N): #미로 입력
        arr[i] = input()
        for j in range(N):
            if arr[i][j] == '2':    #시작점 찾기
                start[0] = i
                start[1] = j

    q.append(start) #시작점 큐에 넣기
    while q:    #큐 내용물이 있는동안
        current = q.pop(0)   #큐의 첫 항목 현재 좌표로 pop <- 너비우선탐색
        for k in range(4):
            ni = current[0] + di[k]
            nj = current[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0: #델타좌표가 인덱스 범위 내에서 방문하지 않은 곳이면
                if arr[ni][nj] == '3':    #3이면 미로 도착
                    result = visited[current[0]][current[1]]
                    token = 1
                    break
                elif arr[ni][nj] == '0':    #0이면 방문표시 후 큐에 추가
                    visited[ni][nj] = visited[current[0]][current[1]] + 1
                    q.append([ni, nj])
        if token == 1:
            break

    print(f'#{tc} {result}')