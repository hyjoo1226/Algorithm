# import sys
# sys.stdin = open('sample_input.txt')

def hex_bin(char):  #16진수 2진수 변환
    hex_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}  # 16진수 딕셔너리
    result = ''
    if char.isdigit() == False:  # A ~ F: 11 ~ 16
        num = hex_dict[char]
    else:
        num = int(char)

    bin = ''  # 변환한 2진수 담을 변수
    while num >= 1:  # 2진수 변환
        bin = str(num % 2) + bin
        num = num // 2
    while len(bin) < 4:  # 16진수 각 자리는 2진수 4자리
        bin = '0' + bin

    result += bin
    return result

def search_password(password):  #암호값 찾기
    if password == ['1', '0', '1', '1', '0', '0', '0']:
        return 0
    elif password == ['1', '0', '0', '1', '1', '0', '0']:
        return 1
    elif password == ['1', '1', '0', '0', '1', '0', '0']:
        return 2
    elif password == ['1', '0', '1', '1', '1', '1', '0']:
        return 3
    elif password == ['1', '1', '0', '0', '0', '1', '0']:
        return 4
    elif password == ['1', '0', '0', '0', '1', '1', '0']:
        return 5
    elif password == ['1', '1', '1', '1', '0', '1', '0']:
        return 6
    elif password == ['1', '1', '0', '1', '1', '1', '0']:
        return 7
    elif password == ['1', '1', '1', '0', '1', '1', '0']:
        return 8
    elif password == ['1', '1', '0', '1', '0', '0', '0']:
        return 9

def check_password(final):  #암호값 검정
    sum1 = final[7] + final[5] + final[3] + final[1]
    sum2 = final[6] + final[4] + final[2]
    if (sum1 * 3 + sum2 + final[0]) % 10 == 0: #10의 배수면 정상
        return sum1 + sum2 + final[0]
    else:   #비정상
        return 0

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())    #NxM 스캐너
    result = 0
    idx_lst = []  # 한번 찾은 암호 다시 안찾도록 좌표 기록
    for i in range(N):
        line = input()  #스캐너 한줄 입력값
        q = []  #16진수 담을 큐
        token = 0   #0아닌 값 등장하면 암호 시작 token 1
        for j in range(M - 1, -1, -1):  #뒤에서부터 0 아닌값 검색
            if line[j] != '0':  #0이 아닌게 나타나면
                if [i - 1, j] in idx_lst:
                    idx_lst.append([i, j])
                else:
                    if token == 0:
                        idx_lst.append([i, j])  #첫 등장 좌표 기록
                    token = 1
            if j >= 1 and line[j] == '0' and line[j - 1] == '0':    #0이 연달아 나오면 암호 끝 token 0
                token = 0

            if token == 1:  #token 1이면(암호면)
                temp = hex_bin(line[j])    #16진수 2진수 변환
                for k in range(3, -1, -1):
                    q.append(temp[k])   #큐에 변환한 2진수 거꾸로 넣기
                if j == 0:  #마지막 인덱스에 도달하면
                    token = 0
            else:   #token 0이면(암호 아니면)
                if q:   #큐 차있으면
                    for b in range(4):
                        q.append('0')
                    code_multi = (len(q)) // 56  # 암호코드의 가로 길이가 몇배 길어지는지
                    while q[0] == '0':  #앞쪽 0 제거
                        q.pop(0)
                    # print(q)
                    # print(len(q))
                    # print('code_mi', code_multi)
                    final = []  #최종 패스워드
                    password = []   #패스워드 1개
                    for a in range(len(q)): #큐 순회하면서
                        password.append(q[a * code_multi])  #패스워드 추가
                        # print(password)
                        if len(password) == 7:  #패스워드 길이가 7이 되면
                            # print(password)
                            final.append(search_password(password))   #패스워드 찾기
                            # print(final)
                            password = []
                            # print(result)
                        if len(final) == 8:
                            if None not in final:
                                result += check_password(final) #암호 검정 후 결과값에 추가
                                # if check_password(final) != 0:
                                #     print(final, check_password(final))
                                q = []
                                # print(result)
                                break

    print(f'#{tc} {result}')



