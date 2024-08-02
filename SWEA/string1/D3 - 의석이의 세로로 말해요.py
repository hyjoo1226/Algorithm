T = int(input())

for test_case in range(1, T + 1):
    str_lst = [['?'] * 15 for _ in range(5)]  # 5x15행렬 '?'값으로 초기화([['?'] * 15] * 5 로 초기화하면 전부 같은 주소를 가리키는 문제 발생)

    for i in range(5):
        temp = input()  #입력된 문자열 temp에 임시저장 - 5번 반복

        for j in range(len(temp)):  #행렬에 temp의 문자열 대입
            str_lst[i][j] = temp[j]

    print(f'#{test_case}', end = ' ')
    for j in range(15):
        for i in range(5):
            if str_lst[i][j] != '?':    #'?'안만나면 출력, 만나면 패스
                print(str_lst[i][j], end = '')
            else:
                pass
    print()
