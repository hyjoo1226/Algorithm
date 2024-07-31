for test_case in range(1, 11):
    N = int(input())    #테스트케이스 번호
    arr = [list(map(int, input().split())) for _ in range(100)]   #배열의 각 행 값 넣은 리스트
    
    max_sum = 0         #최댓값
    dia_sum = 0         #대각선 합(5시방향)
    rev_dia_sum = 0     #대각선 합(7시방향)

    for i in range(100):
        row_sum = 0     #행의 합
        col_sum = 0     #열의 합

        for j in range(100):
            row_sum += arr[i][j]
            col_sum += arr[j][i]
            
            if i == j:
                dia_sum += arr[i][j]
                rev_dia_sum += arr[i][99 - i]

        if max_sum < row_sum:   #기존 최댓값보다 크면 갱신
            max_sum = row_sum
        if max_sum < col_sum:
            max_sum = col_sum

    if max_sum < dia_sum:
        max_sum = dia_sum
    if max_sum < rev_dia_sum:
        max_sum = rev_dia_sum
    
    print(f'#{test_case} {max_sum}')