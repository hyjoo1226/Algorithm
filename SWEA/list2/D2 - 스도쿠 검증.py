def three_square(arr, squ_temp, i, j):
    result = 1
    if arr[i][j] not in squ_temp[i]:
        squ_temp[i] = [x for x in squ_temp[i]] + [arr[i][j]]
    else:
        result = 0
    return result

T = int(input())

for test_case in range(1, T + 1):
    arr = [0] * 9
    for i in range(9):  # 9x9 행렬 초기화 후 입력
        arr[i] = list(map(int, input().split()))
    
    result = 0
    squ_temp = [[] * 9] * 9   #빈 리스트 9개 있는 이중리스트
    #row, col 중복 여부
    for i in range(9):
        row_temp = [0] * 9  #길이 9 리스트 0으로 초기화
        col_temp = [0] * 9
        row_count = 0
        col_count = 0
        check = False   # 2중for문 탈출위한 변수

        for j in range(9):
            if arr[i][j] not in row_temp:   #중복 없으면 temp에 값 추가, count 1 증가
                row_temp[j] = arr[i][j]
                row_count += 1
            if arr[j][i] not in col_temp:
                col_temp[j] = arr[j][i]
                col_count += 1

            if (i < 3) and (j < 3):
                three_square(arr, squ_temp[0], i, j)
                if result == 0:
                    check = True
                    break
            if (i < 3) and (3 <= j < 6):
                three_square(arr, squ_temp[1], i, j)
                if result == 0:
                    check = True
                    break
            if (i < 3) and (6 <= j < 9):
                three_square(arr, squ_temp[2], i, j)
                if result == 0:
                    check = True
                    break
            if (3 <= i < 6) and (j < 3):
                three_square(arr, squ_temp[3], i, j)
                if result == 0:
                    check = True
                    break
            if (3 <= i < 6) and (3 <= j < 6):
                three_square(arr, squ_temp[4], i, j)
                if result == 0:
                    check = True
                    break
            if (3 <= i < 6) and (6 <= j < 9):
                three_square(arr, squ_temp[5], i, j)
                if result == 0:
                    check = True
                    break
            if (6 <= i < 9) and (j < 3):
                three_square(arr, squ_temp[6], i, j)
                if result == 0:
                    check = True
                    break
            if (6 <= i < 9) and (3 <= j < 6):
                three_square(arr, squ_temp[7], i, j)
                if result == 0:
                    check = True
                    break
            if (6 <= i < 9) and (6 <= j < 9):
                three_square(arr, squ_temp[8], i, j)
                if result == 0:
                    check = True
                    break
        if check == True:
            break

        if (row_count == 9) and (col_count == 9):  #모든 count가 9면 중복 아예x, result에 1 대입
            result = 1
        else:   #count가 9가 아닌 경우 중복o, 바로 반복문 종료
            result = 0
            break

print(f'#{test_case} result')