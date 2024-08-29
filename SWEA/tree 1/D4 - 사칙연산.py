def in_order_math(T):
    if T != -1:
        left = graph[T][0] #왼쪽 자식노드
        right = graph[T][1]   #오른쪽 자식노드
        if node[left] in four_cal:    #연산자면 재귀
            in_order_math(left)
        if node[right] in four_cal:
            in_order_math(right)
        if node[left] not in four_cal and node[right] not in four_cal:   #자식 둘 다 숫자면 계산
            if node[T] == '+':
                node[T] = node[left] + node[right]
            elif node[T] == '-':
                node[T] = node[left] - node[right]
            elif node[T] == '*':
                node[T] = node[left] * node[right]
            else:
                node[T] = node[left] / node[right]

for tc in range(1, 11):
    N = int(input())    #정점의 개수
    four_cal = ['+', '-', '*', '/'] #연산자
    graph = [[] for _ in range(N + 1)]
    node = [0] * (N + 1)    #노드 값 기록
    # 트리 만들기
    for i in range(N):
        temp = list(input().split())  #정점이 숫자면 len(temp)는 2, 연산자면 4
        temp[0] = int(temp[0])
        if len(temp) == 2:  #정점 숫자
            node[temp[0]] = int(temp[1]) #해당 노드에 값 추가
        elif len(temp) == 4:  #정점 연산자
            temp[2], temp[3] = int(temp[2]), int(temp[3])
            node[temp[0]] = temp[1]
            graph[temp[0]].append(temp[2])    #해당 노드의 좌우 자식노드 기록
            graph[temp[0]].append(temp[3])
    for i in range(N + 1):  #인덱스 에러 방지
        while len(graph[i]) < 2:
            graph[i].append(-1)
    # print(node)
    # print(graph)
    root = 1    #시작 노드
    in_order_math(root) #중위순회 변형
    result = int(node[1])   #실수 정수로 변환
    print(f'#{tc} {result}')
