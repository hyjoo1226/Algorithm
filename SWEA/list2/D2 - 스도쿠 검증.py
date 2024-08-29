T = int(input())
for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]   #스도쿠 입력
    result = 1
    squ_temp = [[] * 9 for _ in range(9)]   #빈 리스트 9개 있는 이중리스트

    #중복 여부
    for i in range(9):
        row_temp = [0] * 9  #길이 9 리스트 0으로 초기화
        col_temp = [0] * 9

        for j in range(9):
            if arr[i][j] not in row_temp:   #가로 체크
                row_temp[j] = arr[i][j] #중복없으면 리스트에 값 추가
            else:   #중복있으면 result = 0 대입 후 반복문탈출
                result = 0
                break

            if arr[j][i] not in col_temp:   #세로 체크
                col_temp[j] = arr[j][i]
            else:
                result = 0
                break

            square_index = (i // 3) * 3 + (j // 3)  # 3x3 격자 체크
            if arr[i][j] not in squ_temp[square_index]:    #중복없으면 square_lst에 값 추가
                squ_temp[square_index].append(arr[i][j])
            else:
                result = 0  #중복있으면 result에 0 대입 후 반복문탈출
                break
            
        if result == 0: #result가 0이면(중복있으면) 반복문 탈출
            break

    print(f'#{test_case} {result}')