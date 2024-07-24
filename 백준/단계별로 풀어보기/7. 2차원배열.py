#2738 행렬 덧셈

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

#2563 색종이