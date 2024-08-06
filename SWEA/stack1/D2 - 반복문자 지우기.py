T = int(input())

for tc in range(1, T + 1):
    STACKSIZE = 1000
    stack = [0] * STACKSIZE #스택 초기화
    top = -1
    string = input()    #중복제거할 문자열
    result = -1

    for i in range(len(string)):
        if i == 0:  #첫 항 스택에 넣어줌
            top += 1
            stack[top] = string[i]

        elif stack[top] == string[i]:   #중복이 온 경우 top -1(중복값 둘다 스택안에 x)
            top -= 1
            if top == -1 and i == len(string) - 1:  #남은 문자열 없는 경우
                result = 0
                break
        else:   #중복아니면 스택에 넣어줌
            top += 1
            stack[top] = string[i]

    if result != 0:
        result = top + 1

    print(f'#{tc} {result}')
