# 입력값 받을 때 모든 원자들 넘버링(1 ~ N번)하면서 딕셔너리에 추가(ex. 1번원자 = {x, y좌표, 이동방향, 보유에너지, 1번})
# 모든 원자 순회하며 1초 뒤 위치로 업데이트(0.5초 충돌을 고려해 좌표 2배로 늘리기)
# -2000 ~ 2000 좌표 벗어나면 소멸
# 원자 겹치면 해당 시점 기록 후 총에너지에 더해주고 소멸(동시에 여러개 겹치는 경우 구분 위해)
# 소멸하면 딕셔너리에서 제외
# 언제 종료할 것인가? 원자 개수 0이면 종료

T = int(input())
for tc in range(1, T + 1):
    N = int(input())    #원자 개수
    atom_dict = {}  #원자 딕셔너리(번호 = x, y좌표, 방향, 에너지, 번호)
    for i in range(1, N + 1):   #원자 딕셔너리에 추가
        temp = list(map(int, input().split()))
        temp[0] *= 2    #0.5초 충돌 고려
        temp[1] *= 2
        temp.append(i)
        atom_dict[i] = temp

    energy_sum = 0  #에너지 총 합
    while atom_dict:    #원자 있는 동안
        position = {}   #한 사이클 원자 좌표
        atom_remove = []    #제거할 원자 리스트
        for k, v in atom_dict.items():   #모든 원자 순회하면서
            x, y, direc, energy, num = v
            if direc == 0:   #상하좌우 이동
                y += 1
            elif direc == 1:
                y -= 1
            elif direc == 2:
                x -= 1
            else:
                x += 1

            if -2000 > x or 2000 < x or -2000 > y or 2000 < y:  #이 이상 평행하면 안만남
                atom_remove.append(k)  #삭제할 원자 추가

            else:
                if position.get((x, y)) == None:    #해당 좌표에 있는 원자 기록
                    position[(x, y)] = [num]
                else:
                    position[(x, y)].append(num)  #동일 좌표에 있으면 추가
                atom_dict[num] = [x, y, direc, energy, num]  # 해당 원자 좌표 갱신

        for k, v in position.items():
            if len(v) > 1:   #해당 좌표에 원소가 2개 이상이면
                for i in v:
                    energy_sum += atom_dict[i][3]    #에너지 더해주기
                    atom_remove.append(i)

        for item in atom_remove:    #원자 삭제
            temp = atom_dict.pop(item, None)

    print(f'#{tc} {energy_sum}')




