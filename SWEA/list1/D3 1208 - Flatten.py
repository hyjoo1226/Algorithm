for test_case in range(1, 11):
    dump = int(input())
    box_lst = list(map(int, input().split()))

    for i in range(dump):   #가장 큰/낮은 높이와 그 위치를 담을 변수
        num_max = box_lst[0]
        num_min = box_lst[0]
        index_max = 0
        index_min = 0

        for j in range(len(box_lst)):   #가장 큰//낮은 높이와 그 위치를 담는다
            if num_max < box_lst[j]:
                num_max = box_lst[j]
                index_max = j
            if num_min > box_lst[j]:
                num_min = box_lst[j]
                index_min = j

        box_lst[index_max] -= 1 #가장 큰 높이 -1, 낮은 높이 +1
        box_lst[index_min] += 1
    
    final_max = box_lst[0]  #최종 가장 큰/낮은 높이의 값
    final_min = box_lst[0]
    for i in range(len(box_lst)):
        if final_max < box_lst[i]:
            final_max = box_lst[i]
        if final_min > box_lst[i]:
            final_min = box_lst[i]

    result = final_max - final_min   #최고점과 최저점의 높이 차
    print(f'#{test_case} {result}')