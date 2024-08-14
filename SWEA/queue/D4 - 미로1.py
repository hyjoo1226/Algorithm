for tc in range(1, 11):
    num = int(input())  #테케번호
    arr = [[0] * 16 for _ in range(16)] #16x16배열 생성
    visited = [[0] * 16 for _ in range(16)] #방문장소 기록(방문하면1,아니면0)
    q = []  #큐 생성
    start = [-1, -1]  #시작지점
    di = [-1, 1, 0, 0]  #델타좌표 상하좌우
    dj = [0, 0, -1, 1]
    result = 0  #최종결과
    token = 0   #반복문 탈출위한 토큰
    for i in range(16): #미로 입력
        arr[i] = input()
        for j in range(16):
            if arr[i][j] == '2':    #시작점 찾기
                start[0] = i
                start[1] = j

    q.append(start) #시작점 큐에 넣기
    while q:    #큐 내용물이 있는동안
        current = q.pop(0)   #큐의 첫 항목 현재 좌표로 pop <- 너비우선탐색
        for k in range(4):
            ni = current[0] + di[k]
            nj = current[1] + dj[k]
            if 0 <= ni < 16 and 0 <= nj < 16 and visited[ni][nj] == 0: #델타좌표가 인덱스 범위 내에서 방문하지 않은 곳이면
                if arr[ni][nj] == '0':    #0이면 방문표시 후 큐에 추가
                    visited[ni][nj] = 1
                    q.append([ni, nj])
                elif arr[ni][nj] == '3':    #3이면 미로 도착
                    result = 1
                    token = 1
                    break
        if token == 1:
            break

    print(f'#{num} {result}')