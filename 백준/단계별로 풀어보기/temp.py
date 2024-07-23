#별 뒤쪽은 출력 없음
N = int(input())
for i in range(2 * N - 1):
    if i < N:
        print(' ' * (N - i - 1) + '*' * (2 * i + 1))
    else:
        print(' ' * (i - N + 1) + '*' * (4 * N - 2 * i - 3))