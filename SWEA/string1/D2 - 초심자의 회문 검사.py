T = int(input())
for test_case in range(1, T + 1):
    str1 = input().strip()

    check = 0
    for i in range(len(str1)):   #문자열을 순회하며 양 끝 값이 모두 같으면 check = 1
        if str1[i] != str1[len(str1) - 1 - i]:
            check = 0
        else:
            check = 1
    
    print(f'#{test_case} {check}')