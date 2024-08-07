import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    num, E = map(int, input().split())    #테케번호 num, 간선의 개수 E
    adj_matrix = [[0] * 100 for _ in range(100)]    #매트릭스 초기화
    data = list(map(int, input().split()))
    for i in range(E):
        n1 = data[i * 2]
        n2 = data[i * 2 + 1]
        adj_matrix[n1][n2] = 1  #방향그래프이므로

    start = 0
    stack = [start]
    visited = [0] * 100
    result = 0  #경로 존재하면 1 아니면 0
    while stack:
        current = stack.pop()
        if current == 99:   #도착점에 도달하면 종료
            result = 1
            break

        if visited[current] == 0:   #방문 안한 곳이면
            visited[current] = 1
            for next in range(100): #인접한 길 스택에 추가
                if adj_matrix[current][next] == 1 and visited[next] == 0:
                    stack.append(next)

    print(f'#{tc} {result}')