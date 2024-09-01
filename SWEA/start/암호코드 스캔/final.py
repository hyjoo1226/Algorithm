import sys
# sys.stdin = open('sample_input.txt')
sys.stdin = open('new2.txt')
# sys.stdin = open('test.txt')
# F3F033CFCF303C0F33CFCC0F0C3C
# 1111 1100 1111 0000 1100 1100 0011 1111 0011 1111 1100 0000 1100 0011 0000 1111 1100 1100
# 0011 1111 0011 0011 0000 1111 0000 0011 1100 0011
393


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

def search_password(password):  #암호 각 자리 수 찾기
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
    else:
        return -1

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
    result = 0  #최종 결과값
    idx_lst = []  # 암호 시작 좌표 기록
    for i in range(N):
        line = input()  #스캐너 한줄 입력값
        q = []  #16진수 담을 큐
        s_token = 0  # 시작 좌표 기록하면 1
        i_token = 0
        j_token = 0
        last_token = 0
        last_idx = -1  # 끝 좌표
        for j in range(M - 1, -1, -1):  # 뒤에서부터 0 아닌값 검색
            if last_idx != -1:
                if j >= last_idx:
                    continue
                elif j == last_idx - 1 and j > 0: #암호 하나 끝났으므로 변수들 초기화
                    last_idx = -1
                    i_token = 0
                    j_token = 0
                    s_token = 0
                    last_token = 0                    # print(result, q)
                    # q = []
            if line[j] != '0':  # 0이 아닌게 나타나면
                if s_token == 0 and [i - 1, j] in idx_lst:   #아랫줄 겹치는 암호들 처리
                    idx_lst.append([i, j])
                    i_token = 1
                    # print(idx_lst)
                if s_token == 0 and i_token == 0:    # 첫 등장 좌표 기록
                    idx_lst.append([i, j])
                    s_token = 1
                    k = j
                    # print(idx_lst)
                    if j_token == 0:
                        for a in range(j):  #그 좌표로부터 값들 2진수로 변환
                            temp = hex_bin(line[k])
                            for b in range(3, -1, -1):
                                q.append(temp[b])  # 큐에 변환한 2진수 거꾸로 넣기
                            # print(q)
                            k -= 1
                    # print(q)
                    while q[0] == '0':  # 큐 앞쪽 0 제거
                        q.pop(0)
                        last_token += 1
                    # print(q)
                    # print(last_token)
                    pre_pwd = []    #임시 패스워드 담을 리스트
                    pre_pwd2 = []
                    dup = 1 #패스워드 몇번 중복되는지 체크(암호코드가 두꺼워졌는지)
                    while True:
                        q_idx_token = 0
                        q_idx = 0
                        # print(q)
                        # print(dup)
                        for a in range(7): #큐 순회하면서
                            q_idx = (dup - 1) + dup * a
                            if dup > 1:
                                for b in range(dup):
                                    # print('a: ',q_idx, q[q_idx])
                                    # print('b: ',q_idx - b, q[q_idx - b])
                                    if q[q_idx - b] != q[q_idx]:
                                        q_idx_token = 1
                                        # print('달라')
                                        break
                                if q_idx_token == 1:
                                    break
                                else:
                                    pre_pwd.append(q[q_idx])
                            else:
                                pre_pwd.append(q[q_idx])
                                # print(pre_pwd)
                            # print(dup - 1 + dup * a)
                        if search_password(pre_pwd) == -1:  #임시 패스워드가 잘못됐으면 - 암호코드가 두꺼워진 것
                            pre_pwd = []
                        else:
                            # print('pre_pwd: ', pre_pwd)
                            break
                        dup += 1    #몇번 두꺼워진건지 체크

                    final = []  # 최종 패스워드
                    password = []  # 패스워드 1개
                    # print(q)
                    for a in range(len(q)):  # 큐 순회하면서
                        password.append(q[a * dup])  # 패스워드 추가
                        # last_token += dup
                        if len(password) == 7:  # 패스워드 길이가 7이 되면
                            # print(password)
                            final.append(search_password(password))  # 패스워드 찾기
                            password = []
                        if len(final) == 8:
                            result += check_password(final)  # 암호 검정 후 결과값에 추가
                            # temp1 = 4 - last_token
                            last_token += (a * dup)
                            while last_token % 4 != 0:
                                last_token += 1
                            # if last_token == 0:
                            #     last_token = (a * dup) + 1
                            # else:
                            #     while last_token
                            #     last_token = (a * dup) + 5
                            # print(a * dup)
                            # if dup == 1:
                            #     print(q)
                            print(q)
                            print(final, result, dup)
                            # if last_token == 0: #14개 사용
                            #     last_idx = j - 14
                            # else:   #15개 사용
                            #     last_idx = 15
                            last_idx = j - (last_token // 4)
                            # print(last_token)
                            j_token = 1
                            # print(q)
                            q = q[last_token + 1 : ]  #사용하지 않은 부분 큐 재할당
                            # print(q)
                            # print(j, a, dup, last_token, last_idx)
                            # last_idx = j - (a + 1) // 4
                            break
    print(f'#{tc} {result}')

# a = '02F5E65BA316BD78'
# b = '01DB176C588D26EC'
# temp1 = []
# for i in range(14, -1, -1):
#     temp1.append(hex_bin(b[i]))
#     # print(temp)
#     # for j in range(3, -1 ,-1):
#     #     temp1.append(temp[j])
# print(temp1)