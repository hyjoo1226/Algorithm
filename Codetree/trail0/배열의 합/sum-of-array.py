for _ in range(4):
    num_lst = input().split()
    total = 0
    for num in num_lst:
        total += int(num)
    print(total)