from collections import deque


def calculate(type, num):
    if type == 0:
        return num + 1
    elif type == 1:
        return num - 1
    elif type == 2:
        return num * 2
    else:
        return num - 10


def min_cal(num, target):
    visited = set([N])
    q = deque()
    q.append((num, 0))

    while q:
        curr, level = q.popleft()
        if curr == target:
            return level
        for i in range(4):
            tmp = calculate(i, curr)
            if tmp not in visited:
                if tmp <= M + 10 and tmp >= -1:
                    q.append((tmp, level + 1))
                    visited.add(tmp)


T = int(input())

for t in range(1, T + 1):
    # N: 현재 숫자, M: 만들고자 하는 숫자
    N, M = map(int, input().split())

    answer = min_cal(N, M)

    print(f'#{t} {answer}')

# from collections import deque
#
#
# def calculate(type, num):
#     if type == 0:
#         return num + 1
#     elif type == 1:
#         return num - 1
#     elif type == 2:
#         return num * 2
#     else:
#         return num - 10
#
#
# def min_cal(num, target):
#     visited = [0] * 1000003
#     q = deque()
#     q.append((num, 0))
#     visited[num] = 1
#
#     while q:
#         curr, level = q.popleft()
#         if curr == target:
#             return level
#         for i in range(4):
#             tmp = calculate(i, curr)
#             if (tmp <= 1000000 or tmp >= -1) and not visited[tmp]:
#                 q.append((tmp, level + 1))
#                 visited[tmp + 1] = 1
#
#
# T = int(input())
#
# for t in range(1, T + 1):
#     # N: 현재 숫자, M: 만들고자 하는 숫자
#     N, M = map(int, input().split())
#
#     answer = min_cal(N, M)
#
#     print(f'#{t} {answer}')

# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())    #시작 N, 끝 M
#     q = deque()
#     if N * 32 < M:
#         while N * 2 < M:
#             N = N * 2
#     q.append(N)
#     visited = set([N])
#     level = 0
#     token = 0
#     while q:
#         temp = []
#         while q:
#             current = q.pop()
#             visited.add(current)
#             if current + 1 == M:
#                 level += 1
#                 token = 1
#                 break
#             else:
#                 if (current + 1) >= -1 and (current + 1) <= M + 10 and (current + 1) not in visited:
#                     temp.append(current + 1)
#             if current - 1 == M:
#                 level += 1
#                 token = 1
#                 break
#             else:
#                 if (current - 1) >= -1 and (current - 1) <= M + 10 and (current + 1) not in visited:
#                     temp.append(current - 1)
#             if current * 2 == M:
#                 level += 1
#                 token = 1
#                 break
#             else:
#                 if (current * 2) >= 0 and (current * 2) <= M + 10 and (current + 1) not in visited:
#                     temp.append(current * 2)
#             if current - 10 == M:
#                 level += 1
#                 token = 1
#                 break
#             else:
#                 if (current - 10) >= -1 and (current - 10) <= M + 10 and (current + 1) not in visited:
#                     temp.append(current - 10)
#         if token == 1:
#             break
#         q = temp[:]
#         level += 1
#     print(f'#{tc} {level}')