T = int(input())
for tc in range(1, T + 1):
    stick_str = input() #괄호레이저 담긴 문자열
    stick_str_len = len(stick_str)  #문자열의 길이

    stack = [0] * stick_str_len #스택 생성
    stack[0] = stick_str[0]
    top = 0

    count = 0   #조각 개수 합
    first_stick = 0 #레이저에 한번도 안잘린 막대기 개수
    if stack[0] == '(':
        first_stick = 1

    for i in range(1, stick_str_len):  #문자열 순회하면서
        if stick_str[i - 1] == '(' and stick_str[i] == ')': #여는괄호 닫는괄호 만나면 레이저 완성
            top -= 1    #여는괄호 1개 레이저용으로 제외
            first_stick -= 1
            if top != -1:   #스택에 여는괄호 남아있으면 카운트에 추가
                count += (first_stick * 2) + (top - first_stick + 1)    #레이저에 처음 잘리는 막대인 경우 x2, 아닌 경우 +1
                first_stick = 0
        elif stick_str[i] == ')':   #닫는괄호 연달아 나오면 막대기 하나 끝난 것
            top -= 1
        elif stick_str[i] == '(': #여는괄호 만나면 스택에 추가
            top += 1
            stack[top] = '('
            first_stick += 1

    print(f'#{tc} {count}')