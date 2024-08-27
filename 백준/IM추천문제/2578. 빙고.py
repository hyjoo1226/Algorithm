def bingo_check(arr):   #빙고면 true, 아니면 false 리턴
    bingo_count = 0 #빙고카운트
    for i in range(5):
        width_count = 0
        length_count = 0
        for j in range(5):  #가로체크
            if arr[i][j] == 0:
                width_count += 1
                if width_count == 5:
                    bingo_count += 1
            else:
                width_count = 0

            if arr[j][i] == 0:  #세로체크
                length_count += 1
                if length_count == 5:
                    bingo_count += 1
            else:
                length_count = 0
    #대각체크
    if arr[0][0] == 0 and arr[1][1] == 0 and arr[2][2] == 0 and arr[3][3] == 0 and arr[4][4] == 0:
        bingo_count += 1
    if arr[0][4] == 0 and arr[1][3] == 0 and arr[2][2] == 0 and arr[3][1] == 0 and arr[4][0] == 0:
        bingo_count += 1
        
    if bingo_count >= 3:
        return True
    else:
        return False



arr = [[0] * 5 for _ in range(5)]
for i in range(5):  #빙고판 입력
    arr[i] = list(map(int, input().split()))

call_num = []
for i in range(5):  #사회자가 부르는 수 하나의 리스트로
    temp = list(map(int, input().split()))
    call_num.extend(temp)

token = 0
for k in range(1, 26):
    for i in range(5):
        for j in range(5):  #빙고판에서
            if arr[i][j] == call_num[k - 1]:   #사회자가 부른 수 0으로 체크
                arr[i][j] = 0
                result = bingo_check(arr)
                if result == True:
                    print(k)
                    token = 1
                    break
        if token == 1:
            break
    if token == 1:
        break