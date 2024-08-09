from pprint import pprint

"""
5
13001
10100
11000
11110
10020
"""

def search_stack(N, arr, stack):
    if len(stack) == 0:  # 스택이 비었다면(미로 탈출x). return 0
        return 0
    current = stack.pop()  # 현재 위치
    arr[current[0]][current[1]] = 1    #방문한 장소는 1로 체크
    di = [-1, 1, 0, 0]  #상하좌우
    dj = [0, 0, -1, 1]

    for k in range(4):  # 현재 위치에서 델타좌표(상하좌우)를 갔을 때
        if (0 <= current[0] + di[k] < N) and (0 <= current[1] + dj[k] < N) and (arr[current[0] + di[k]][current[1] + dj[k]] != 1): #인덱스 범위내에서
            if arr[current[0] + di[k]][current[1] + dj[k]] == '3':   #3이면 목적지. return 1
                return 1
            if arr[current[0] + di[k]][current[1] + dj[k]] == '0':   #0이면 해당 좌표 스택에 추가
                stack.append([current[0] + di[k], current[1] + dj[k]])
    return search_stack(N, arr, stack)  #재귀 호출

T = int(input())

for tc in range(1, T + 1):
    N = int(input())    #NxN배열 초기화
    arr = [[0] * N for _ in range(N)]
    for i in range(N):
        temp = input().strip()
        for j in range(N):
            arr[i][j] = temp[j]

    start = [-1, -1]  #시작 좌표
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                start[0] = i
                start[1] = j
                break
    stack = [start] #스택 시작좌표로 초기화

    result = search_stack(N, arr, stack)
    print(f'#{tc} {result}')


# def search_stack(N, arr, stack):    #탐색 후 0인 인덱스 스택에 추가, 3이면 미로 끝
#     if len(stack) == 0:  # 스택이 비었다면(미로 탈출x). return 0
#         return 0
#     current = stack.pop()  # 현재 위치
#     arr[current[0]][current[1]] = 1    #방문한 장소는 1로 체크
#     di = [-1, 1, 0, 0]  #상하좌우
#     dj = [0, 0, -1, 1]
#     for k in range(4):  #현재 위치에서 델타좌표(상하좌우)를 갔을 때
#         if arr[current[0] + di[k]][current[1] + dj[k]] == '3':   #3이면 목적지. return 1
#             return 1
#         if arr[current[0] + di[k]][current[1] + dj[k]] == '0':   #0이면 해당 좌표 스택에 추가
#             stack.append([current[0] + di[k], current[1] + dj[k]])
#     return search_stack(N, arr, stack)  #재귀 호출
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())    #(N+2)x(N+2)배열 초기화(입력값배열에 테두리추가)
#     arr = [[7] * (N + 2) for _ in range(N + 2)]
#     for i in range(1, N + 1):
#         temp = input()
#         for j in range(1, N + 1):
#             arr[i][j] = temp[j - 1]
#
#     start = [-1, -1]  #시작 좌표
#     for i in range(N + 1):
#         for j in range(N + 1):
#             if arr[i][j] == '2':
#                 start[0] = i
#                 start[1] = j
#                 break
#
#     stack = [start] #스택 시작좌표로 초기화
#
#     result = search_stack(N, arr, stack)
#     print(f'#{tc} {result}')


# def search_stack(N, arr, stack):   #탐색 후 0인 인덱스 스택에 추가, 3이면 미로 끝
#     if len(stack) == 0: #스택이 비면
#         return 0
#     current = stack.pop()   #현재 위치
#     arr[current[0]][current[1]] = -1    #방문한 장소는 -1로 체크
#     #상하좌우 0 있으면 해당 좌표 추가
#     if (current[0] - 1) > -1:   #상
#         if arr[current[0] - 1][current[1]] == '0':
#             stack.append([current[0] - 1, current[1]])
#         if arr[current[0] - 1][current[1]] == '3':
#             return 1
#     if (current[0] + 1) < N:   #하
#         if arr[current[0] + 1][current[1]] == '0':
#             stack.append([current[0] + 1, current[1]])
#         if arr[current[0] + 1][current[1]] == '3':
#             return 1
#     if (current[1] - 1) > -1:   #좌
#         if arr[current[0]][current[1] - 1] == '0':
#             stack.append([current[0], current[1] - 1])
#         if arr[current[0]][current[1] - 1] == '3':
#             return 1
#     if (current[1] + 1) < N:   #우
#         if arr[current[0]][current[1] + 1] == '0':
#             stack.append([current[0], current[1] + 1])
#         if arr[current[0]][current[1] + 1] == '3':
#             return 1
#
#     return search_stack(N, arr, stack)
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())    #NxN배열 초기화
#     arr = [[0] * N for _ in range(N)]
#     for i in range(N):
#         temp = input()
#         for j in range(N):
#             arr[i][j] = temp[j]
#
#     start = [-1, -1]  #시작 좌표
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == '2':
#                 start[0] = i
#                 start[1] = j
#                 break
#     stack = [start] #스택 시작좌표로 초기화
#
#     result = search_stack(N, arr, stack)
#     print(f'#{tc} {result}')
