def pre_order(node):    #순회
    global cnt
    if node != -1:
        cnt += 1
        pre_order(graph[node][0])
        pre_order(graph[node][1])

T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())    #간선의 개수 E, 노드 N을 루트로 하는 서브 트리
    graph = [[] for _ in range(E + 2)]
    temp = list(map(int, input().split()))
    for i in range(E):  #인접리스트 만들기
        graph[temp[i * 2]].append(temp[(i * 2) + 1])

    for i in range(E + 2):  #index 오류 방지
        while len(graph[i]) < 2:
            graph[i].append(-1)

    cnt = 0   #서브 트리 노드 개수
    pre_order(N)
    print(f'#{tc} {cnt}')
