N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    num_sum = 0
    for i in range(a, b + 1):
        if i % 2 == 0:
            num_sum += i
    print(num_sum)