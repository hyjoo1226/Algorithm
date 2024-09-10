T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split()) #NxM 초기 상태(용기의 크기는 무한해서 -인 경우도 확장가능해야, 배양 시간 K)
    cell_dict = {}  # key:(세포 좌표), value(생명력, 비활성시간, 활성시간(비활성일 때는 0)) 저장할 딕셔너리
    for i in range(N):
        temp = list(map(int, input().split()))  #초기 상태 한줄
        for j in range(M):
            if temp[j] != 0:
                cell_dict[(i, j)] = [temp[j], temp[j], 0] #초기 상태 딕셔너리 입력(줄기세포 있는 곳만(0값이 아닌 곳만)

    di = [1, -1, 0, 0]  #상하좌우 델타좌표
    dj = [0, 0, 1, -1]
    for t in range(K):    #배양 시간 동안
        new_cell = {}   #이번 시간에 새로 추가된 세포
        for k, (HP, inact, act) in cell_dict.items():  #딕셔너리 순회하면서
            if inact > 0:    #비활성시간이 있다면 -1
                inact -= 1
                cell_dict[k][1] = inact
                # cell_dict[k][1] -= 1  이렇게 쓸 경우 얕은복사
                if inact == 0:  #비활성시간이 0이 되면 활성상태로 전환
                    cell_dict[k][2] = HP #활성시간에 생명력만큼 부여

            if inact == 0 and act == HP:  #활성상태로 전환됐을때 번식
                    for a in range(4):  #델타 탐색
                        nx = k[0] + di[a]
                        ny = k[1] + dj[a]
                        if cell_dict.get((nx, ny)) == None and new_cell.get((nx, ny)) == None: #델타 좌표가 두 딕셔너리에 없으면
                            new_cell[(nx, ny)] = [HP, HP, 0] #동일한 생명력을 value로 새로 추가된 세포 딕셔너리에 추가
                        elif new_cell.get((nx, ny)) != None:   #동시에 번식된 경우
                            if new_cell[(nx, ny)][0] < HP: #먼저 추가한 생명력이 더 작다면 큰 값으로 갱신
                                new_cell[(nx, ny)] = [HP, HP, 0]

            if act > 0:  #활성상태라면 활성시간 -1
                act -= 1
                cell_dict[k][2] = act
                # cell_dict[k][2] -= 1

        cell_dict.update(new_cell)  #딕셔너리 업데이트

    cnt = 0 #살아있는 줄기세포 개수
    for (HP, inact, act) in cell_dict.values():
        if inact > 0 or act > 0:  #줄기세포 살아있다면(비활성상태 or 활성상태)
            cnt += 1

    print(f'#{tc} {cnt}')
