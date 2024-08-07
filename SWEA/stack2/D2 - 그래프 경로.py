T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())    # 노드 V, 간선의 개수 E
    matrix = [[0] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        i, j = map(int, input().split())
        matrix[i][j] = 1
    start, end = map(int, input().split())

    stack = [start]
    visited = [0] * (V + 1)
    result = 0
    while stack:
        current = stack.pop()
        if current == end:  #경로가 존재
            result = 1
            break
        if visited[current] == 0:
            visited[current] = 1
            for next in range(V + 1):
                if matrix[current][next] == 1 and visited[next] == 0:
                    stack.append(next)

    print(f'#{tc} {result}')