T = int(input())

for test_case in range(1, T + 1):
    N, K = list(map(int, input().split()))

    arr = [0] * N
    for i in range(N):
        arr[i] = list(map(int, input().split()))


    