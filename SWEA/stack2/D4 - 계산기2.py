for tc in range(1, 11):
    length = int(input())   #문자열 계산식의 길이
    calc = input()  #문자열 계산식
    post_calc = []  #후위표기법 리스트
    stack = []  #변환 과정에 사용할 스택
    dict_calc = {'+':1, '*':2}  #연산자 우선순위

    #후위 표기식으로 변환
    for i in range(length):
        if dict_calc.get(calc[i]) == None:  #연산자가 아니면
            post_calc.append(calc[i])   #후위표기법 리스트에 추가
        else:   #연산자면
            if stack == []: #스택이 비어있으면 임시 스택에 추가
                stack.append(calc[i])
            elif dict_calc[calc[i]] > dict_calc[stack[-1]]:   #연산자의 우선순위가 더 높다면
                stack.append(calc[i])   #임시 스택에 추가
            else:   #연산자의 우선순위가 더 낮아질때까지 스택에서 pop
                while stack != [] and dict_calc[calc[i]] <= dict_calc[stack[-1]]:
                    post_calc.append(stack.pop())   #후위표기법 리스트로 pop
                stack.append(calc[i])
        if stack != [] and i == length - 1: #마지막 항목 추가
            while stack != []:
                post_calc.append(stack.pop())

    #계산
    stack = []  #스택 초기화
    for item in post_calc:
        if dict_calc.get(item) == None: #연산자가 아니면 스택에 추가
            stack.append(int(item))
        else:   #연산자면
            B = stack.pop() #연산자 뒤 숫자
            A = stack.pop() #연산자 앞 숫자
            if item == '+':
                stack.append(A + B) #연산 결과 스택에 추가
            else:
                stack.append(A * B)

    print(f'#{tc} {stack[0]}')