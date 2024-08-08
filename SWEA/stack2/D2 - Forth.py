T = int(input())
for tc in range(1, T + 1):
    post_calc = list(input().split())
    stack = []  #스택 생성
    calc_lst = ['+', '-', '*', '/'] #연산자 리스트
    result = 0  #결과값

    for item in post_calc:
        if item == '.':   #'.'가 오면 코드가 끝난다
            break

        if item not in calc_lst:    #연산자가 아니면
            stack.append(item)  #스택에 추가
        else:   #연산자면
            if len(stack) == 1: #스택에 숫자가 하나인경우 error(후위표기법은 숫자 두개 이후 연산자가 오므로)
                result = 'error'
                break

            B = int(stack.pop())  # 연산자 뒤 숫자
            A = int(stack.pop())  # 연산자 앞 숫자

            if item == '+': #나누기 외 연산자
                stack.append(A + B)
            elif item == '-':
                stack.append(A - B)
            elif item == '*':
                stack.append(A * B)
            else:   #나누기
                if A == 0:  # 0을 나누면 에러
                    result = 'error'
                    break
                else:
                    stack.append(A // B)
    if len(stack) != 1: #연산자가 더 없는데 스택에 숫자가 두개 이상 남아있거나 스택이 빈 경우 error
        result = 'error'

    if result == 'error':
        print(f'#{tc} {result}')
    else:
        result = stack[0]
        print(f'#{tc} {result}')
