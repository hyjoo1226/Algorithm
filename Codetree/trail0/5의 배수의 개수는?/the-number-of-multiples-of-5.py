total = 0

for _ in range(4):
    num_lst = input().split()
    for num in num_lst:
        if int(num) % 5 == 0:
            total += 1

print(total)