def solution(p):
    if p == '': #입력이 빈 문자열인 경우, 빈 문자열 반환
        return ''

    token = [0, 0]
    u = ''
    for i in range(len(p)): #두 균형잡힌 문자열로 분리
        if p[i] == '(':
            token[0] += 1
            u += '('
        else:
            token[1] += 1
            u += ')'
        if token[0] == token[1]:
            v = p[i + 1 : ]
            break

    top = -1
    cor = 1 #cor이 0이면 올바르지 않은 문자열, 1이면 올바른 문자열
    for i in range(len(u)): #올바른 괄호 문자열인지 검사
        if top == -1 and u[i] == ')':
            cor = 0
            break
        if top != -1 and u[i] == ')':
            top -= 1
        if u[i] == '(':
            top += 1

    if cor == 1:    #올바른 문자열이면
        u += solution(v)
        return u
    else:   #올바른 문자열이 아니면
        s = '('
        s += solution(v)
        s += ')'
        u = u[1 : len(u) - 1]
        for c in u:
            if c == '(':
                s += ')'
            else:
                s += '('
        return s