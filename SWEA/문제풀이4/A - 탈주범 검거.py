# import sys
from pprint import pprint
# sys.stdin = open('sample_input.txt')

def search_tunnel(current):
    dx = [-1, 1, 0, 0]  # 상하좌우 델타좌표
    dy = [0, 0, -1, 1]
    t_type = current[2] #터널 타입
    for k in range(4):
        nx = current[0] + dx[k]
        ny = current[1] + dy[k]
        if nx < 0 or nx >= N or ny < 0 or ny >= M or visited[nx][ny] == 1 or arr[nx][ny] == 0:  #인덱스 범위 내에서 방문 안한 곳이고 터널 있을 때
            continue
        if t_type == 2 and (k == 2 or k == 3):  #터널 연결된 경우 스택에 추가
            continue
        if t_type == 2 and k == 0 and (arr[nx][ny] == 3 or arr[nx][ny] == 4 or arr[nx][ny] == 7):
            continue
        if t_type == 2 and k == 1 and (arr[nx][ny] == 3 or arr[nx][ny] == 5 or arr[nx][ny] == 6):
            continue
        if t_type == 3 and (k == 0 or k == 1):
            continue
        if t_type == 3 and k == 2 and (arr[nx][ny] == 2 or arr[nx][ny] == 6 or arr[nx][ny] == 7):
            continue
        if t_type == 3 and k == 3 and (arr[nx][ny] == 2 or arr[nx][ny] == 4 or arr[nx][ny] == 5):
            continue
        if t_type == 4 and (k == 1 or k == 2):
            continue
        if t_type == 4 and k == 0 and (arr[nx][ny] == 3 or arr[nx][ny] == 4 or arr[nx][ny] == 7):
            continue
        if t_type == 4 and k == 3 and (arr[nx][ny] == 2 or arr[nx][ny] == 4 or arr[nx][ny] == 5):
            continue
        if t_type == 5 and (k == 0 or k == 2):
            continue
        if t_type == 5 and k == 3 and (arr[nx][ny] == 2 or arr[nx][ny] == 4 or arr[nx][ny] == 5):
            continue
        if t_type == 5 and k == 1 and (arr[nx][ny] == 3 or arr[nx][ny] == 5 or arr[nx][ny] == 6):
            continue
        if t_type == 6 and (k == 0 or k == 3):
            continue
        if t_type == 6 and k == 1 and (arr[nx][ny] == 3 or arr[nx][ny] == 5 or arr[nx][ny] == 6):
            continue
        if t_type == 6 and k == 2 and (arr[nx][ny] == 2 or arr[nx][ny] == 6 or arr[nx][ny] == 7):
            continue
        if t_type == 7 and (k == 1 or k == 3):
            continue
        if t_type == 7 and k == 2 and (arr[nx][ny] == 2 or arr[nx][ny] == 6 or arr[nx][ny] == 7):
            continue
        if t_type == 7 and k == 0 and (arr[nx][ny] == 3 or arr[nx][ny] == 4 or arr[nx][ny] == 7):
            continue
        if [nx, ny, arr[nx][ny]] not in q:
            q.append([nx, ny, arr[nx][ny]])

T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())   #NxM배열, (R,C) 맨홀 위치, 소요시간L
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]   #방문기록
    q = [[R, C, arr[R][C]]]  #좌표, 터널 타입 큐
    q_len = 1
    cnt = 0
    while q:
        if L == 0:
            break
        for i in range(q_len):
            current = q.pop(0) #현재위치
            visited[current[0]][current[1]] = 1
            cnt += 1
            search_tunnel(current)
        L -= 1
        q_len = len(q)

    print(f'#{tc} {cnt}')




#
# def search_tunnel(N, L, current):  #연결된 터널을 스택에 넣어준다
#     dx = [-1, 1, 0, 0]    #상하좌우 델타좌표
#     dy = [0, 0, -1, 1]
#     t_type = current[2] #터널 타입
#     if L == 1:  #시간 마지막이면 바로 종료
#         return
#     for k in range(4):
#         nx = current[0] + dx[k]
#         ny = current[1] + dy[k]
#         if nx < 0 or nx >= N or ny < 0 or ny >= M or visited[nx][ny] == 1 or arr[nx][ny] == 0:  #인덱스 범위 내에서 방문 안한 곳이고 터널 있을 때
#             continue
#         if t_type == 2 and (k == 2 or k == 3):  #터널 연결된 경우 스택에 추가
#             continue
#         if t_type == 2 and k == 0 and (arr[nx][ny] == 3 or arr[nx][ny] == 4 or arr[nx][ny] == 7):
#             continue
#         if t_type == 2 and k == 1 and (arr[nx][ny] == 3 or arr[nx][ny] == 5 or arr[nx][ny] == 6):
#             continue
#         if t_type == 3 and (k == 0 or k == 1):
#             continue
#         if t_type == 3 and k == 2 and (arr[nx][ny] == 2 or arr[nx][ny] == 6 or arr[nx][ny] == 7):
#             continue
#         if t_type == 3 and k == 3 and (arr[nx][ny] == 2 or arr[nx][ny] == 4 or arr[nx][ny] == 5):
#             continue
#         if t_type == 4 and (k == 1 or k == 2):
#             continue
#         if t_type == 4 and k == 0 and (arr[nx][ny] == 3 or arr[nx][ny] == 4 or arr[nx][ny] == 7):
#             continue
#         if t_type == 4 and k == 3 and (arr[nx][ny] == 2 or arr[nx][ny] == 4 or arr[nx][ny] == 5):
#             continue
#         if t_type == 5 and (k == 0 or k == 2):
#             continue
#         if t_type == 5 and k == 3 and (arr[nx][ny] == 2 or arr[nx][ny] == 4 or arr[nx][ny] == 5):
#             continue
#         if t_type == 5 and k == 1 and (arr[nx][ny] == 3 or arr[nx][ny] == 5 or arr[nx][ny] == 6):
#             continue
#         if t_type == 6 and (k == 0 or k == 3):
#             continue
#         if t_type == 6 and k == 1 and (arr[nx][ny] == 3 or arr[nx][ny] == 5 or arr[nx][ny] == 6):
#             continue
#         if t_type == 6 and k == 2 and (arr[nx][ny] == 2 or arr[nx][ny] == 6 or arr[nx][ny] == 7):
#             continue
#         if t_type == 7 and (k == 1 or k == 3):
#             continue
#         if t_type == 7 and k == 2 and (arr[nx][ny] == 2 or arr[nx][ny] == 6 or arr[nx][ny] == 7):
#             continue
#         if t_type == 7 and k == 0 and (arr[nx][ny] == 3 or arr[nx][ny] == 4 or arr[nx][ny] == 7):
#             continue
#         stack.append([nx, ny, arr[nx][ny]])
#         hole(N, L - 1)
#
# def hole(N, L):
#     global cnt
#     if stack != [] and L == 1:
#         cnt += 1
#         temp = stack.pop()
#         visited[temp[0]][temp[1]] = 1
#         return
#     elif stack == []:    #기저조건: 스택 x / 시간 L
#         return
#     elif L == 1:
#         return
#     current = stack.pop()   #현재 좌표, 터널 타입
#     visited[current[0]][current[1]] = 1 #방문표시
#     cnt += 1
#
#     search_tunnel(N, L, current)
#     hole(N, L - 1)
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M, R, C, L = map(int, input().split())   #NxM배열, (R,C) 맨홀 위치, 소요시간L
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     visited = [[0] * M for _ in range(N)]   #방문기록
#     stack = [[R, C, arr[R][C]]]  #좌표, 터널 타입 스택
#     #시작점: R,C / 시간 1
#     #끝점: 스택 x / 시간 L
#     cnt = 0 #위치할 수 있는 장소의 수
#     hole(N, L)
#
#     print(f'#{tc} {cnt}')