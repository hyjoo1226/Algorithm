N = int(input())
friend_num = 0

for i in range(1, N + 1):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        continue
    friend_num += 1

print(friend_num)