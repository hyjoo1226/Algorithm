T = int(input())
for tc in range(1, T + 1):
    N = int(input())    #당근 개수
    C_lst = list(map(int, input().split())) #당근의 크기 담긴 리스트
    count = 1   #연속으로 커지는 값(최소 1)
    max_count = 1   #최대값
    for i in range(N - 1):
        if C_lst[i] < C_lst[i + 1]:
            count += 1
        else:   #연속끊기면
            if max_count < count:
                max_count = count
            count = 1
    if max_count < count:   #마지막 연속 안 끊긴 경우
        max_count = count

    print(f'#{tc} {max_count}')