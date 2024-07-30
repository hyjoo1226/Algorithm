T = int(input())

for test_case in range(1 , T + 1):
    width = int(input())    #가로의 길이
    box_lst = list(map(int, input().split()))   #쌓여있는 상자의 수 리스트
    result = 0  #낙차

    for i in range(width):
        first_height = -1   #각 가로줄 처음 나타나는 상자(가장 높이 위치한 상자)
        count = 0   #각 가로줄 상자 개수
        for j in range(len(box_lst)):
            if box_lst[j] > i:
                if first_height == -1:
                    first_height = len(box_lst) - j
                count += 1
        print(first_height)
        # print(count)
        if result < first_height - count:   #낙차 구하기
            result = first_height - count

    # print(f'#{test_case} {result}')

