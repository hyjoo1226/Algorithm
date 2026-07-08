N = int(input())
n_sum = 0

for i in range(1, 101):
    n_sum += i
    if n_sum >= N:
        print(i)
        break