T = int(input())

for tc in range(1, T + 1):
    K, N, M = input().split()
    charge_station = list(map(int, input().split()))    #충전소
    K = int(K)  #한번 충전으로 최대한 이동할 수 있는 정류장의 수
    N = int(N)  #정류장 수 (N은 종점)
    M = int(M)  #충전소 개수

    charge = K  # 충전량
    idx = 0 #현재위치(시작점으로 초기화)
    charge_count = 0   #충전횟수
    result = -1 #최종값
    max_charge = 0  # 도달할 수 있는 가장 큰 충전소

    while idx < N:  #현재 위치가 종점에 도달하기 전까지
        if idx + K >= N:
            break
        temp = []   #현재 위치에서 도달가능한 모든 충전소
        for item in charge_station:
            if idx + K >= item and item > idx:
                temp.append(item)
        if temp == []:  #도달가능 x면
            result = 0
            break
        else:
            idx = temp[-1]   #도달할 수 있는 가장 큰 충전소
            charge_count += 1
    if result != 0:
        result = charge_count
    print(f'#{tc} {result}')
     
#스택사용 - 시간초과 문제 발생
    # charge = K  #충전량
    # idx = 0 #현재위치(시작점으로 초기화)
    # station = list(range(0, N + 1)) #모든 정류장
    # stack = [0] * M  #도착한 충전소
    # top = -1    #스택 끝 위치
    # use_stack = []  #사용한 충전소
    # result = -1  #최종값
    #
    # while charge > 0:
    #     idx += 1    #한칸 이동하고, 충전 1 감소
    #     charge -= 1
    #
    #     if idx == N:    #종점 도착하면 반복문 탈출
    #         break
    #
    #     if station[idx] in charge_station:  #충전소 도착한다면 스택에 추가
    #         top += 1
    #         stack[top] = station[idx]
    #
    #     if charge == 0: #종점 도착 못했는데 충전이 0이되면
    #         if top == -1:   #스택(충전소)이 비어있다면 종점 도착 x. result = 0
    #             result = 0
    #             break
    #         else:   #스택이 있다면
    #             idx = stack[top]   #마지막 도착한 충전소로 이동
    #             top -= 1
    #             charge = K  #충전
    #             use_stack.append(idx)   #사용한 충전소에 추가
    #
    # if result == 0: #종점 도착x 경우
    #     print(f'#{tc} {result}')
    # else:   #종점 도착한 경우
    #     result = len(use_stack)
    #     print(f'#{tc} {result}')