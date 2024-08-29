import sys
sys.stdin = open('input.txt')

def search_password(password):  #암호값 찾기
    if password == [0, 0, 0, 1, 1, 0, 1]:
        return 0
    elif password == [0, 0, 1, 1, 0, 0, 1]:
        return 1
    elif password == [0, 0, 1, 0, 0, 1, 1]:
        return 2
    elif password == [0, 1, 1, 1, 1, 0, 1]:
        return 3
    elif password == [0, 1, 0, 0, 0, 1, 1]:
        return 4
    elif password == [0, 1, 1, 0, 0, 0, 1]:
        return 5
    elif password == [0, 1, 0, 1, 1, 1, 1]:
        return 6
    elif password == [0, 1, 1, 1, 0, 1, 1]:
        return 7
    elif password == [0, 1, 1, 0, 1, 1, 1]:
        return 8
    elif password == [0, 0, 0, 1, 0, 1, 1]:
        return 9

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())    #NxM배열
    token = 0   #입력값은 계속 받아야 하므로
    for i in range(N):
        temp = input()  #입력값 한줄
        if token == 0:
            idx = -1 #마지막 1 위치
            for j in range(M - 1, 55, -1):
                if temp[j] == '1':    #그 줄에 1이 있는지 검사
                    idx = j
                    break
            if idx != -1:   #1이 있었다면
                start = idx - 55    #암호 시작위치
                final_password = [] #최종 암호
                password = [0, 0, 0, 0, 0, 0, 0]   #암호 1개 기록
                count = 0   #7의배수
                for k in range(start, idx + 1): #암호해석
                    password[count % 7] = int(temp[k])
                    if k != start and count % 7 == 0:   #암호 1개 찼으면 최종 암호에 추가
                        final_password.append(search_password(password))
                    count += 1
                final_password.append(search_password(password))
                token = 1

    result = 0
    sum1, sum2 = 0, 0   #암호검정, 잘못된 암호면 result 0
    for i in range(8):
        if i % 2 == 0:
            sum1 += final_password[i]
        else:
            sum2 += final_password[i]
    if ((sum1 * 3) + sum2) % 10 == 0:   #올바른 암호
        result = sum1 + sum2

    print(f'#{tc} {result}')
