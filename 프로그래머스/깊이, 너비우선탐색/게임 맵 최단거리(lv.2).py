from collections import deque

def solution(maps):
    answer = 0
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    n = len(maps)
    m = len(maps[0])
    
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        
        while queue:
            x, y = queue.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    if nx == n - 1 and ny == m - 1:
                        return maps[nx][ny]
                    queue.append((nx, ny))
        return -1
        
    answer = bfs(0, 0)
        
    return answer