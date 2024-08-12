T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split()) #사람의 수 N, M초의 시간을 들여 K개의 붕어빵
    person = list(map(int, input().split()))    #사람 도착시간 리스트

    for i in range(0, N - 1): #리스트 오름차순 선택정렬
        min_idx = i
        for j in range(i, N):
            if person[min_idx] > person[j]:
                min_idx = j
        person[min_idx], person[i] = person[i], person[min_idx]

    bread = 0   #붕어빵 개수
    sec = 0 #시간경과
    result = 'Possible' #결과
    while person:
        if person[0] == 0:  #오픈하자마자 사람이 오면
            result = 'Impossible'
            break
        sec += 1    #시간 + 1
        if sec % M == 0:    #빵 만들어지는 시간
            bread += K  #빵 개수 추가
        while sec in person:   #해당 시간에 오는 사람이 있는동안
            if bread == 0:  #빵이 없다면
                result = 'Impossible'
                break
            person.pop(0)
            bread -= 1
        if person == [] or result == 'Impossible':    #사람 붕어빵 다 제공했으면
            break

    print(f'#{tc} {result}')
