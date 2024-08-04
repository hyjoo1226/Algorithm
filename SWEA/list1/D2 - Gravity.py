T = int(input())

for test_case in range(1 , T + 1):
    width = int(input())    #가로의 길이
    box_lst = list(map(int, input().split()))   #쌓여있는 상자의 수 리스트
    result = 0  #낙차

    highest_box = 0    #가장 높은 박스
    for item in box_lst:
        if highest_box < item:
            highest_box = item

    arr = [[0] * highest_box for _ in range(9)]  #배열 0으로 초기화 후 매핑
    for i in range(9):
        for j in range(highest_box):
            if j <= box_lst[i - 1]:
                arr[i][j] = 1

    for i in range(9):
        for j in range(highest_box):
            if j <= box_lst[i - 1]:
                for i in range(1, 9):
                arr[i][j]

        

