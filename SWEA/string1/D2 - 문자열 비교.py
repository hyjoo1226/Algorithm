T = int(input())

for test_case in range(1, T + 1):
    str1 = input()  #작은 문자열    
    str2 = input()  #긴 문자열

    check = 0
    for i in range(len(str2)):
        if i + len(str1) <= len(str2):
            if str2[i : i + len(str1)] == str1: #긴 문자열을 작은 문자열의 길이만큼 슬라이스한게 작은 문자열과 일치하는 경우
                check = 1

    print(f'#{test_case} {check}')
