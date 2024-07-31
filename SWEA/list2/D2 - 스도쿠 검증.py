T = int(input())

for test_case in range(1, T + 1):
    arr = [0] * 9
    for i in range(9):  # 9x9 행렬 초기화 후 입력
        arr[i] = list(map(int, input().split()))
    
    result = 0
    #row, col 중복 여부
    for i in range(9):
        row_temp = [0] * 9  #길이 9 리스트 0으로 초기화
        col_temp = [0] * 9
        row_count = 0
        col_count = 0

        for j in range(9):
            if arr[i][j] not in row_temp:   #중복 없으면 temp에 값 추가, count 1 증가
                row_temp[j] = arr[i][j]
                row_count += 1
            if arr[j][i] not in col_temp:
                col_temp[j] = arr[j][i]
                col_count += 1
        
        if (row_count == 9) and (col_count == 9):  #모든 count가 9면 중복 아예x, result에 1 대입
            result = 1
        else:   #count가 9가 아닌 경우 중복o, 바로 반복문 종료
            result = 0
            break
    #3x3씩 9개 중복 여부
    # arr2 = [[0] * 9] * 9
    # for i in range(9):
    #     for j in range(9):
    #         if i < 3:
    #             if j < 3:
    #                 arr2[]
    #             elif j < 6:
    #             else:



    