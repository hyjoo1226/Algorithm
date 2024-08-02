def mirror_str(char):   #문자 바꾸는 함수
    if char == 'b':
        return 'd'
    if char == 'd':
        return 'b'
    if char == 'p':
        return 'q'
    if char == 'q':
        return 'p'

T = int(input())

for test_case in range(1, T + 1):
    str1 = input()

    print(f'#{test_case}', end = ' ')
    for i in range(len(str1)):  #문자열의 끝부터 앞쪽으로 순회하면서
        if i == len(str1) - 1:
            print(mirror_str(str1[-i - 1]))
        else:
            print(mirror_str(str1[-i - 1]), end = '')