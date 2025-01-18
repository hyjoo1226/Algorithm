from collections import deque


A, B = map(int, input().split())    #A 수빈이, B 동생
visited = [0] * 100001  # 방문 체크(방문한 곳에 다시 가면 빠른 시간이 아니므로)
queue = deque([(A, 0)]) # 시작 위치 큐

while queue:   # 큐 있는 동안
    current, depth = queue.popleft()   # 큐 하나 꺼내기 - BFS
    visited[current] = 1    # 방문체크

    if current == B:    # 찾으면 종료
        print(depth)
        break

    A_F = current + 1   # 앞으로 이동
    if 0 <= A_F <= 100000 and visited[A_F] == 0:  # 못찾았는데 방문안했고 범위 내면 큐에 추가
        queue.append((A_F, depth + 1))

    A_B = current - 1   # 뒤로 이동
    if 0 <= A_B <= 100000 and visited[A_B] == 0:
        queue.append((A_B, depth + 1))

    A_T = current * 2   # 순간이동
    if 0 <= A_T <= 100000 and visited[A_T] == 0:
        queue.append((A_T, depth + 1))