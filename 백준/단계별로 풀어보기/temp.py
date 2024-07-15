str = input()
alpha = {}
for s in str:
    alpha[s] = 0
    if alpha ==
    alpha[s] += 1


# str = input()
# alpha = list(range(52))

# for i in alpha:
#     alpha[i] = 0
# for s in str:
#     alpha[ord(s) - ord('A')] += 1

# count = 0
# alpha.sort()
# print(alpha)
# if alpha[-1] == alpha[-2]:
#     print('?')
# else:
#     print(alpha[-1])


# happy의 pp처럼 붙어있는 경우 해결해야함
# count = 0
# N = int(input())
# for i in range(N):
#     str = input()
#     alpha = list(range(26))
#     for i in alpha:
#         alpha[i] = 0
#     token = 1
#     for s in str:
#         if alpha[ord(s) - ord('a')] == 1:
#             token = 0
#             break
#         alpha[ord(s) - ord('a')] = 1
#     if token == 1:
#         count += 1
# print(count)

