for tc in range(1, 11):
    length = int(input())   #문자열 계산식의 길이
    calc = input()  #문자열 계산식
    post_calc = []  #후위표기법 리스트
    stack = []  #변환 과정에 사용할 스택

    #후위 표기식으로 변환
    for i in range(length):
        if calc[i] != '+':  #연산자가 아니면
            post_calc.append(calc[i])   #후위표기법 리스트에 추가
        else:   #연산자면
            stack.append(calc[i])   #임시 스택에 추가
            if len(stack) == 2: #임시 스택의 크기가 2이면(우선순위 같으므로 1이어야만 함)
                post_calc.append(stack.pop())   #후위표기법 리스트로 pop
        if i == length - 1: #마지막 항목 추가
            post_calc.append(stack.pop())

    #계산
    stack = []  #스택 초기화
    for item in post_calc:
        if item != '+': #연산자가 아니면 스택에 추가
            stack.append(int(item))
        else:   #연산자면
            B = stack.pop() #연산자 뒤 숫자
            A = stack.pop() #연산자 앞 숫자
            stack.append(A + B) #연산 결과 스택에 추가

    print(f'#{tc} {stack[0]}')