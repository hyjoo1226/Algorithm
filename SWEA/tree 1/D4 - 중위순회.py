def in_order(node): #중위순회 - 재귀
    if node:    #left[node] / right[node]가 0을 가리키면(하위 노드가 없으면) 조건문 진입 x 
        in_order(left[node])
        print(par[node], end='')    #알파벳으로 출력
        # print(node, end='')   #숫자로 출력
        in_order(right[node])

for tc in range(1, 11):
    N = int(input())    #정점의 개수 N
    par = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for i in range(N):  #배열로 풀기
        temp = list(input().split())    #임시저장
        temp[0] = int(temp[0])
        par[temp[0]] = temp[1]  #각 정점이 가진 알파벳 저장
        if len(temp) > 2:
            left[temp[0]] = int(temp[2]) #정점에 연결된 좌우노드 기록
            if len(temp) == 4:
                right[temp[0]] = int(temp[3])

    root = 1    #루트 노드는 1
    print(f'#{tc}', end=' ')
    in_order(root)
    print()