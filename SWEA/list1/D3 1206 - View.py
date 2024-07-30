for test_case in range(1, 11):
    N = int(input())    #건물의 개수
    height_lst = list(map(int, input().split()))    #건물의 높이
    view = 0
    result = 0

    for i in range(N):
        if (i > 1) and (i < (N - 2)):   #양 옆 2건물보다 크다면
            if ((height_lst[i] > height_lst[i - 2]) and (height_lst[i] > height_lst[i - 1]) and (height_lst[i] > height_lst[i + 1]) and (height_lst[i] > height_lst[i + 2])):
                highest = height_lst[i - 2]     #양 옆 2건물 중 가장 높은 높이
                for x in [-1, 1, 2]:
                    if highest < height_lst[i + x]:
                        highest = height_lst[i + x]
                view = height_lst[i] - highest     #해당 건물의 조망권 확보된 세대수
                result += view

    print(f'#{test_case} {result}')