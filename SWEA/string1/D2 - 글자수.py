T = int(input())

for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()

    str_dict = {}   #빈 딕셔너리 생성
    for char in str1:
        if char not in str_dict:    #해당 문자가 딕셔너리 키에 없다면 0의 밸류를 가지고 추가
            str_dict[char] = 0
    
    for char in str2:   #str2를 순회하면서
        if char in str_dict:    #해당 문자가 딕셔너리 키에 있다면
            str_dict[char] += 1 #해당 키의 밸류값 1 증가

    max_value = 0   #딕셔너리의 가장 큰 밸류 구하기
    for k, v in str_dict.items():
        if max_value < v:
            max_value = v

    print(f'#{test_case} {max_value}')