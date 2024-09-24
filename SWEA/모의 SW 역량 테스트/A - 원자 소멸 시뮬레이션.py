# 입력값 받을 때 모든 원자들 넘버링(1 ~ N번)하면서 딕셔너리에 추가(ex. 1번원자 = {x, y좌표, 이동방향, 보유에너지})
# 모든 원자 순회하며 1초 뒤 위치로 업데이트
# 만약 그 과정에서 겹치면 해당 시점 기록 후 총에너지에 더해주고 소멸(동시에 여러개 겹치는 경우 구분 위해)
# 소멸하면 딕셔너리에서 제외 or 에너지값 0으로 변경
# 언제 종료할 것인가? 위치진행방향 따로 기록한 딕셔너리 처음에 만들어둬야할듯
# 테케 50개중 12개 정답(시간초과)

def is_validation(x_direction, y_direction):    #충돌할 원자 남아있는지 검증
    temp = []
    for k, v in x_direction.items():
        if v[0] >= 1 and v[1] >= 1:   #같은 좌표계에 충돌할 원자 존재하면
            return 1    #충돌할 원자 남아있음 -> 1 리턴
        else:   #없다면 딕셔너리에서 제외
            temp.append(k)
    for item in temp:
        x_direction.pop(item)

    temp = []
    for k, v in y_direction.items():
        if v[0] >= 1 and v[1] >= 1:
            return 1
        else:
            temp.append(k)
    for item in temp:
        y_direction.pop(item)

    return 0    #충돌할 원자 x -> 0 리턴

T = int(input())
for tc in range(1, T + 1):
    N = int(input())    #원자 개수
    atom_dict = {}  #원자 딕셔너리(번호 = x, y좌표, 방향, 에너지, 번호)
    x_direction = {}  #상하 마주치는 좌표의 원자개수 기록
    y_direction = {}  #좌우

    for i in range(1, N + 1):   #원자 딕셔너리에 추가
        temp = list(map(int, input().split()))
        temp[0] *= 2    #0.5초 충돌 고려
        temp[1] *= 2
        temp.append(i)
        atom_dict[i] = temp
        if (atom_dict[i][2] == 0 or atom_dict[i][2] == 1):   #상, 하로 움직이는 원자인 경우
            if x_direction.get(atom_dict[i][0]) == None:  #x좌표 같은데 방향성 다른 것 기록
                x_direction[atom_dict[i][0]] = [0, 0]
            if atom_dict[i][2] == 0:
                x_direction[atom_dict[i][0]][0] += 1
            else:
                x_direction[atom_dict[i][0]][1] += 1
        else:   #좌, 우의 경우
            if y_direction.get(atom_dict[i][1]) == None:  #y좌표
                y_direction[atom_dict[i][1]] = [0, 0]
            if atom_dict[i][2] == 2:
                y_direction[atom_dict[i][1]][0] += 1
            else:
                y_direction[atom_dict[i][1]][1] += 1

    energy_sum = 0  #에너지 총 합
    while is_validation(x_direction, y_direction) == 1:    #충돌할 원자 있는 동안
        position = {}   #한 사이클 원소 좌표
        for k, v in atom_dict.items():   #모든 원소 순회하면서
            x, y, direc, energy, num = v
            if direc == 0:   #상하좌우 이동
                y += 1
            elif direc == 1:
                y -= 1
            elif direc == 2:
                x -= 1
            else:
                x += 1

            if position.get((x, y)) == None:    #해당 좌표에 있는 원자 기록
                position[(x, y)] = [num]
            else:
                position[(x, y)].append(num)  #동일 좌표에 있으면 추가
            atom_dict[num] = [x, y, direc, energy, num]  # 해당 원소 좌표 갱신

        for k, v in position.items():
            if len(v) > 1:   #해당 좌표에 원소가 2개 이상이면
                for i in v:
                    energy_sum += atom_dict[i][3]    #에너지 더해주기
                    temp = atom_dict.pop(i)  #원소 소멸
                    if temp[2] == 0:    #x,y_direction에서도 빼주기
                        if temp[0] in x_direction:
                            x_direction[temp[0]][0] -= 1
                    elif temp[2] == 1:
                        if temp[0] in x_direction:
                            x_direction[temp[0]][1] -= 1
                    elif temp[2] == 2:
                        if temp[1] in y_direction:
                            y_direction[temp[1]][0] -= 1
                    elif temp[2] == 3:
                        if temp[1] in y_direction:
                            y_direction[temp[1]][0] -= 1

    print(f'#{tc} {energy_sum}')




