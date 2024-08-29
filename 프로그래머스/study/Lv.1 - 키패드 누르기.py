#   왼 * 7 4 1
#   중 0 8 5 2
#   우 # 9 6 3
#중앙으로 엄지이동 고려해야함
def solution(numbers, hand):
    answer = ''
    l_idx = 0   #왼손 위치
    r_idx = 0   #오른손 위치
    l_dict = {7 : 1, 4 : 2, 1 : 3}    #왼쪽 키패드 딕셔너리
    r_dict = {9 : 1, 6 : 2, 3 : 3}  #오른쪽 키패드 딕셔너리
    c_dict = {0 : 0, 8 : 1, 5 : 2, 2 : 3}   #중앙 키패드 딕셔너리
    for item in numbers:    #각 번호마다
        l = 0   #왼손이면 1, 오른손이면 0
        c = 0   #중앙이면 1, 아니면 0
        if l_dict.get(item) != None:    #왼쪽이면
            l = 1
        elif c_dict.get(item) != None:  #중앙인 경우
            c = 1
            if abs(l_idx - c_dict[item]) < abs(r_idx - c_dict[item]):   #왼쪽이 더 가까우면
                l = 1
            elif abs(l_idx - c_dict[item]) == abs(r_idx - c_dict[item]):    #거리 같으면
                if hand == 'left':
                    l = 1

        if l == 1:  #왼쪽이면 값 갱신하고, 왼손 위치 변경
            answer += 'L'
            if c == 1:
                l_idx = c_dict[item]
            else:
                l_idx = l_dict[item]
        else:
            answer += 'R'
            if c == 1:
                r_idx = c_dict[item]
            else:
                r_idx = r_dict[item]

    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))