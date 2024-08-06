for tc in range(1, 11):
    N, num_str = input().split()
    print(N)
    print(num_str)
    stack = [0] * 100   #스택 초기화
    top = -1

    for i in range(int(N)):
        if i == 0:  #첫 항 스택에 넣어줌
            top += 1
            stack[top] = num_str[i]

        elif stack[top] == num_str[i]:    #중복인 경우 제외
            top -= 1

        else:   #중복이 아니면 스택에 넣어줌
            top += 1
            stack[top] = num_str[i]

    print(f'#{tc}', end = ' ')  #stack의 0번째부터 top까지 출력
    for i in range(0, top + 1):
        print(stack[i], end = '')
    print()