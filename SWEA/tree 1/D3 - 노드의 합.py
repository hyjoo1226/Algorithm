def post_order_sum(L):  #자식노드 합친 값 부모노드에 넣기
    if L != -1:
        left = graph[L][0]
        right = graph[L][1]

        post_order_sum(left)
        post_order_sum(right)
        if left != -1 and right != -1:  #자식노드 둘 다 있으면
            node[L] = node[left] + node[right]
        elif left != -1:    #자식노드 한개만 있으면
            node[L] = node[left]
        else:   #자식노드 없으면
            pass

T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split()) #노드 개수 N, 리프노드 개수 M, 출력할 노드 번호 L
    graph = [[] for _ in range(N + 1)]  #tree 인접리스트
    node = [0] * (N + 1)    #값 저장

    # tree 인접리스트 만들기
    idx = 2
    while True:
        for i in range(1, N + 1):
            while idx < N + 1 and len(graph[i]) < 2:
                graph[i].append(idx)
                idx += 1
            if idx == N + 1:
                break
        if idx == N + 1:
            break
    for i in range(N + 1):  #인덱스 에러 방지
        while len(graph[i]) < 2:
            graph[i].append(-1)

    for i in range(M):
        a, b = map(int, input().split())    #리프노드 번호 a, 값 b
        node[a] = b #값 저장

    post_order_sum(L)   #출력할 노드번호로 함수 호출
    print(f'#{tc} {node[L]}')