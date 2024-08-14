from pprint import pprint

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())    #정점 개수 V, 노드 개수 E
    arr = [[0] * (V + 1) for _ in range(V + 1)]   #V+1 배열, 정점끼리 이어지면 1, 아니면 0
    for i in range(E):
        a, b = map(int, input().split())
        arr[a][b] = 1   #무방향그래프
        arr[b][a] = 1
    S, G = map(int, input().split())    #출발 S, 도착 G
    visited = [0] * (V + 1) #방문장소
    result = 0  #최종결과

    q = [S]  #출발위치 담긴 큐
    count = 0   #노드 이동 횟수
    while q:   #큐가 있는동안
        temp = []   #임시저장
        while q:    #현재 큐가 빌 때까지(큐 비어도 도착못하면 count 1 증가 후 다음 큐 사이클로)
            current = q.pop(0)   #current에 큐의 첫 항목 pop
            if current == G:    #도착하면 이동횟수 결과저장 후 반복문 종료
                result = count
                break
            if visited[current] == 0:   #방문안한곳이면
                visited[current] = 1    #방문표시
                for next in range(V + 1):
                    if arr[current][next] == 1 and visited[next] == 0:  #연결된 정점 중 방문안한곳이면 temp에 추가
                        temp.append(next)
        if result != 0: #도착하면 반복문 종료
            break
        q = temp    #temp에 임시저장한 값 큐로 옮김(다음사이클)
        count += 1

    print(f'#{tc} {result}')
