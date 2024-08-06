T = int(input())

for tc in range(1, T + 1):
    A = input() #괄호검사할 문자열
    STACKSIZE = 500
    stack = [0] * STACKSIZE #스택생성
    top = -1
    result = 1  #괄호 짝 맞으면 1, 아니면 0

    for char in A:
        if char == '(': #왼쪽괄호면 top + 1, 스택에 추가
            top += 1
            stack[top] = '('
        elif char == '{':
            top += 1
            stack[top] = '{'
        elif char == ')':   #오른쪽괄호면
            if top == -1:   #스택이 비어있다면 result = 0
                result = 0
                break
            else:   #스택의 top이 짝이 맞으면
                if stack[top] == '(':
                    top -= 1
                else:   #짝이 안맞으면 result = 0
                    result = 0
                    break
        elif char == '}':
            if top == -1:
                result = 0
                break
            else:
                if stack[top] == '{':
                    top -= 1
                else:
                    result = 0
                    break
    if top != -1:   #스택에 값이 남아있으면
        result = 0

    print(f'#{tc} {result}')