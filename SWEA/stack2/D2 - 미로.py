def search_stack(N, arr, stack):   #탐색 후 0인 인덱스 스택에 추가, 3이면 미로 끝
    current = stack.pop()   #현재 위치
    arr[current[0]][current[1]] = -1    #방문한 장소는 -1로 체크
    #상하좌우 0 있으면 해당 좌표 추가
    if (current[0] - 1) > -1:   #상
        if arr[current[0] - 1][current[1]] == '0':
            stack.append([current[0] - 1, current[1]])
        if arr[current[0] - 1][current[1]] == '3':
            return 1
    if (current[0] + 1) < N:   #하
        if arr[current[0] + 1][current[1]] == '0':
            stack.append([current[0] + 1, current[1]])
        if arr[current[0] + 1][current[1]] == '3':
            return 1
    if (current[1] - 1) > -1:   #좌
        if arr[current[0]][current[1] - 1] == '0':
            stack.append([current[0], current[1] - 1])
        if arr[current[0]][current[1] - 1] == '3':
            return 1
    if (current[1] + 1) < N:   #우
        if arr[current[0]][current[1] + 1] == '0':
            stack.append([current[0], current[1] + 1])
        if arr[current[0]][current[1] + 1] == '3':
            return 1
    print(stack)
    if len(stack) == 0: #스택이 비면
        return 0
    return search_stack(N, arr, stack)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())    #NxN배열 초기화
    arr = [[0] * N for _ in range(N)]
    for i in range(N):
        temp = input()
        for j in range(N):
            arr[i][j] = temp[j]

    start = [N - 1, -1]  #시작 좌표
    for i in range(N):
        if arr[N - 1][i] == '2':
            start[1] = i
            break
    stack = [start] #스택 시작좌표로 초기화

    result = search_stack(N, arr, stack)
    print(f'#{tc} {result}')
