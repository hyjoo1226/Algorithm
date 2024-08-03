import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    arr = [0] * 9
    for i in range(9):  # 9x9 행렬 초기화 후 입력
        arr[i] = list(map(int, input().split()))
    
    result = 1
    squ_temp = [[] * 9] * 9   #빈 리스트 9개 있는 이중리스트

    #row, col 중복 여부
    for i in range(9):
        row_temp = [0] * 9  #길이 9 리스트 0으로 초기화
        col_temp = [0] * 9

        for j in range(9):
            if arr[i][j] not in row_temp:   #행에 중복 없으면 temp에 값 추가
                row_temp[j] = arr[i][j]
            else:   #중복있으면 result = 0 대입 후 반복문탈출
                result = 0
                break

            if arr[j][i] not in col_temp:   #열
                col_temp[j] = arr[j][i]
            else:   
                result = 0
                break

            square_index = (i // 3) * 3 + (j // 3)  # 3x3 작은 격자 중복여부
            if arr[i][j] not in squ_temp[square_index]:    #중복없으면 square_lst에 값 추가
                squ_temp[square_index] = [x for x in squ_temp[square_index]] + [arr[i][j]]
            else:
                result = 0  #중복있으면 result에 0 대입 후 반복문탈출
                break
            
        if result == 0: #result가 0이면(중복있으면) 반복문 탈출
            break

    print(f'#{test_case} {result}')