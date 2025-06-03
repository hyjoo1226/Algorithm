from itertools import permutations

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
max_sum = -1

for perm in permutations(num_list, 3):
    num_sum = 0
    count = 0
    for i in perm:
        if num_sum + i > M:
            break
        num_sum += i
        count += 1

    if count == 3:
        max_sum = max(max_sum, num_sum)

print(max_sum)