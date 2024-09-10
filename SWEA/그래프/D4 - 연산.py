from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())    #시작 N, 끝 M
    q = deque()
    if N * 32 < M:
        while N * 2 < M:
            N = N * 2
    q.append(N)
    visited = set([N])
    level = 0
    token = 0
    while q:
        temp = []
        while q:
            current = q.pop()
            visited.add(current)
            if current + 1 == M:
                level += 1
                token = 1
                break
            else:
                if (current + 1) >= -1 and (current + 1) <= M + 10 and (current + 1) not in visited:
                    temp.append(current + 1)
            if current - 1 == M:
                level += 1
                token = 1
                break
            else:
                if (current - 1) >= -1 and (current - 1) <= M + 10 and (current + 1) not in visited:
                    temp.append(current - 1)
            if current * 2 == M:
                level += 1
                token = 1
                break
            else:
                if (current * 2) >= 0 and (current * 2) <= M + 10 and (current + 1) not in visited:
                    temp.append(current * 2)
            if current - 10 == M:
                level += 1
                token = 1
                break
            else:
                if (current - 10) >= -1 and (current - 10) <= M + 10 and (current + 1) not in visited:
                    temp.append(current - 10)
        if token == 1:
            break
        q = temp[:]
        level += 1
    print(f'#{tc} {level}')