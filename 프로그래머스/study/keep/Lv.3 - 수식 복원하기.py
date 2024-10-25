def ab_cvt(save_num1, save_num2, i):    #진법 변환한 값 리턴
    a = ''
    b = ''
    num1 = save_num1
    num2 = save_num2
    while num1:  # 더할 두 수 진법변환
        a = str(num1 % i) + a
        num1 = num1 // i
    while num2:
        b = str(num2 % i) + b
        num2 = num2 // i
    return a, b

def cal(a, b, pm, i):   #연산 결과 리턴
    if pm == '+':   # 더하기
        temp = list(str(int(a) + int(b)))
        for j in range(len(temp) - 1, -1, -1):  # 자릿수 바뀌는 부분 처리
            if int(temp[j]) >= i:
                if j != 0:
                    temp[j] = str(int(temp[j]) - i)
                    temp[j - 1] = str(int(temp[j - 1]) + 1)
                else:
                    temp[j] = str(int(temp[j]) - i)
                    temp.insert(0, '1')
    else:   # 빼기
        a = list(a[::-1])  # 문자열 뒤집고 리스트로 변환
        b = list(b[::-1])
        print(a)
        print(b)
        len_a = len(a)
        len_b = len(b)
        temp = []
        for j in range(len_b):
            if a[j] < b[j]:
                if a[j + 1] == '0': #다음 자리도 0이면
                    p = 1
                    while a[j + p] != '0':  #0 아닌 값 나오는 위치 찾기
                        p += 1
                    p += 1
                    while p > 0:
                        a[j + p] = str(int(a[j + p]) - 1)
                        a[j + p - 1] = str(i)
                        p -= 1
                    temp.append(str(int(a[j]) - int(b[j])))
                else:
                    a[j + 1] = str(int(a[j + 1]) - 1)
                    temp.append(str(int(a[j]) + i - int(b[j])))
            else:
                temp.append(str(int(a[j]) - int(b[j])))
        for k in range(len_b, len_a):
            temp.append(a[k])
        temp.reverse()
    return temp


def cvt(num1, num2, num3, pm, possible):    #연산결과 10진수로 다시 변환 후 값이 일치하면 사용가능 진법
    save_num1 = num1
    save_num2 = num2
    new_possible = []
    for i in possible:
        a, b = ab_cvt(save_num1, save_num2, i)
        print(a, b)
        c = int(''.join(cal(a, b, pm, i)), i)
        # print('a, b, 계산, c:', a, b, cal(a, b, pm, i), c, i)
        if c == num3:  # 변환 값이 일치하면 사용가능 진법
            new_possible.append(i)
    possible = new_possible[:] #new_possible로 교체


def solution(expressions):
    answer = []
    ans = []  # X 없는 수식
    que = []  # X 있는 수식
    possible = []  # 가능한 진법
    result = [] #최종 X값
    num_min = 99999999  #가장 작은 연산값 저장
    for item in expressions:  # 수식 구분
        if item.split()[-1] != 'X' and int(item.split()[-1]) < num_min:
            num_min = int(item.split()[-1])
        if item[-1] == 'X':  # X들어간 수식이면
            que.append(item)
        else:
            ans.append(item)
    for i in range(2, 10):  #가장 작은 연산값보다 큰 값은 진법에서 제외
        if i <= num_min:
            possible.append(i)

    for item in ans:  # 각 수식 숫자 3개 전처리
        temp = list(item.split())
        cvt(int(temp[0]), int(temp[2]), int(temp[-1]), temp[1], possible)

    for item in que:    #가능한 진법으로 X계산
        temp = list(item.split())
        for pos in possible:
            a, b = ab_cvt(int(temp[0]), int(temp[2]), pos)
            c = int(''.join(cal(a, b, temp[1], pos)), pos)
            if c not in result: #가능한 값들 리스트에 추가
                result.append(c)

        if len(result) == 1:    #값이 하나면
            temp[-1] = str(result[0])
        else:   #값이 여러개면
            temp[-1] = '?'

        answer.append(' '.join(temp))    #최종 값에 추가
    print('answer:', answer)
    return answer

a = ["14 + 3 = 17", "13 - 6 = X", "51 - 5 = 44"]
solution(a)