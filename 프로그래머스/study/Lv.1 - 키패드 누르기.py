def solution(numbers, hand):
    answer = ''
    pad = [['*', 7, 4, 1], [0, 8, 5, 2], ['#', 9, 6, 3]]    #키패드 이차원배열
    l_idx = [0, 0]   #왼손 위치
    r_idx = [2, 0]  #오른손 위치

    for item in numbers:    #입력한 숫자들 순회
        for i in range(3):  #pad에서 위치 검색
            for j in range(4):
                if pad[i][j] == item:   #위치 찾았을 때
                    if i == 0:  #왼손이 처리
                        l_idx = [i, j]
                        answer += 'L'
                    elif i == 2:    #오른손이 처리
                        r_idx = [i, j]
                        answer += 'R'
                    else:   #중앙인 경우
                        l = abs(i - l_idx[0]) + abs(j - l_idx[1])   #왼손 거리
                        r = abs(i - r_idx[0]) + abs(j - r_idx[1])   #오른손 거리
                        if l < r:   #왼손이 더 가까우면
                            l_idx = [i, j]
                            answer += 'L'
                        elif l > r: #오른손이 더 가까우면
                            r_idx = [i, j]
                            answer += 'R'
                        else:   #거리 같으면
                            if hand == 'left':  #왼손잡이면
                                l_idx = [i, j]
                                answer += 'L'
                            else:   #오른손잡이면
                                r_idx = [i, j]
                                answer += 'R'

    return answer
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# hand = 'right'
# print(solution(numbers, hand))