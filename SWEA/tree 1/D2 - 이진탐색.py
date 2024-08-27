def in_order(node): #중위순회
    if node != -1:
        in_order(graph[node][0])
        in_order_graph.append(node)
        in_order(graph[node][1])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())    #1 ~ N 자연수, 노드의 개수 N

    graph = [[] for _ in range(N + 1)]
    k = 1
    cnt = 1 #정점 추가될때마다 cnt + 1
    while k < N + 1:    #인접리스트 만들기(모든 정점 돌 때까지)
        cnt += 1
        if cnt > N:
            break
        graph[k].append(cnt)

        cnt += 1
        if cnt > N:
            break
        graph[k].append(cnt)
        k += 1

    for i in range(N + 1):  #index 오류 방지
        while len(graph[i]) < 2:
            graph[i].append(-1)

    in_order_graph = [] #중위순회 순서기록
    root = 1    #루트노드
    in_order(root) #중위순회

    root_value = 0  #루트노드에 기록된 값
    n2_value = 0    #N/2번 노드에 기록된 값
    for i in range(N):
        if in_order_graph[i] == 1:
            root_value = i + 1
        if in_order_graph[i] == N // 2:
            n2_value = i + 1
        if root_value != 0 and n2_value != 0:   #두개 값 다 찾았으면 반복문 종료
            break

    print(f'#{tc} {root_value} {n2_value}')
