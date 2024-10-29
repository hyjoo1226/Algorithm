#2738 행렬 덧셈
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        a[i][j] += b[i][j]

for i in range(n):
    print(*a[i])
# for i in range(n):
#     for j in range(m):
#         print(a[i][j], end=' ')
#     print('')

#2566 최댓값
num_max = -1
target = []
for i in range(9):
    num_lst = list(map(int, input().split()))
    for j in range(len(num_lst)):
        if num_lst[j] > num_max:
            num_max = num_lst[j]
            target.clear()
            target.append(i + 1)
            target.append(j + 1)
print(num_max)
print(target[0], target[1])

#10798 세로읽기
arr = [[] for _ in range(5)]

for i in range(5):
    arr[i] = list(input())
    while len(arr[i]) < 15:
        arr[i].append('@')

for i in range(15):
    for j in range(5):
        if arr[j][i] != '@':
            print(arr[j][i], end='')

#2563 색종이
arr = [[0] * 100 for _ in range(100)]
n = int(input())
for k in range(n):
    a, b = map(int, input().split())
    for i in range(b, b + 10):
        for j in range(a, a + 10):
            arr[i][j] = 1
paper = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            paper += 1
print(paper)