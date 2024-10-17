def cvt(num1, num2, num3, pm, possible):
    save_num1 = num1
    save_num2 = num2
    if possible == []:  #진법 목록이 없는 경우
        for i in range(2, 10):  # 2 ~ 9 진법변환
            a = ''
            b = ''
            num1 = save_num1
            num2 = save_num2
            while num1: #더할 두 수 진법변환
                a = str(num1 % i) + a
                num1 = num1 // i
            while num2:
                b = str(num2 % i) + b
                num2 = num2 // i

            if pm == '+':
                temp = list(str(int(a) + int(b))) # 두 수 더하고 빼기
            else:
                temp = list(str(int(a) - int(b)))

            for j in range(len(temp)-1, -1, -1):    #자릿수 바뀌는 부분 처리
                if int(temp[j]) >= i:
                    if j != 0:
                        temp[j] = str(int(temp[j]) - i)
                        temp[j - 1] = str(int(temp[j - 1]) + 1)
                    else:
                        temp[j] = str(int(temp[j]) - i)
                        temp.insert(0, '1')
            c = ''.join(temp)
            c = int(c, i)   #10진수로 변환
            if c == num3:   #변환 값이 일치하면 사용가능한 진법
                possible.append(i)

    else:   #진법 목록이 있다면 그 진법만 사용
        for i in possible:
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
            if pm == '+':
                temp = list(str(int(a) + int(b)))  # 두 수 더하고 빼기
            else:
                temp = list(str(int(a) - int(b)))
            print(a)
            print(b)

            for j in range(len(temp) - 1, -1, -1):  # 자릿수 바뀌는 부분 처리
                if int(temp[j]) >= i:
                    if j != 0:
                        temp[j] = str(int(temp[j]) - i)
                        temp[j - 1] = str(int(temp[j - 1]) + 1)
                    else:
                        temp[j] = str(int(temp[j]) - i)
                        temp.insert(0, '1')
            c = ''.join(temp)
            c = int(c, i)  # 10진수로 변환
            if c != num3:   #변환 값이 일치하지 않으면 사용불가 진법
                possible.remove(i)

            


def solution(expressions):
    answer = []
    ans = []    #X 없는 수식
    que = []    #X 있는 수식
    possible = []   #가능한 진법
    for item in expressions:  #수식 구분
        if item[-1] == 'X': # X들어간 수식이면
            que.append(item)
        else:
            ans.append(item)

    for item in ans:    #각 수식 숫자 3개 전처리
        temp = list(item.split())
        cvt(int(temp[0]), int(temp[2]), int(temp[-1]), temp[1], possible)
        print(possible)

    return answer

a = ["14 + 3 = 17", "13 - 6 = X", "51 - 5 = 44"]
solution(a)