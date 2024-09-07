T = int(input())
for tc in range(1, T + 1):
    N = int(input())    #NxN 배열 디저트카페들
    arr = [[list(map(int, input().split()))] for _ in range(N)]
    di = [1, 1, -1, -1] #대각 시계방향 델타좌표
    dj = [1, -1, -1, 1]


