def height_result(height, temp, i, n):
    if height[i] - height[i + n] > 0:
        if temp == 0:
            temp = height[i] - height[i + n]
        if temp > height[i] - height[i + n]:
            temp = height[i] - height[i + n]
        return temp
    else:
        return 0

for test_case in range(10):
    N = int(input())
    height = list(map(int, input().split()))
    height_lst = []

    for i in range(N):
        if (i > 1) and (i < (N - 2)):
            temp = 0

            for n in [-2, -1, 1, 2]:
                temp = height_result(height, temp, i, n)
            # print(temp)
            height_lst.append(temp)
    print(height_lst)
    height_sum = 0
    for number in height_lst:
        height_sum += number

    print(f'#{test_case} {height_sum}')