T = int(input())
for tc in range(1, T + 1):
    N = int(input())    #두 정수가 N번
    bus = []
    Cj_lst = []
    for i in range(N):
        bus.append(list(map(int, input().split())))
    P = int(input())    #하나의 정수 P번
    for i in range(P):
        Cj_lst.append(int(input()))

    result = []
    for i in range(P):
        count = 0
        for j in range(N):
            if bus[j][0] <= Cj_lst[i] <= bus[j][1]:
                count += 1
        result.append(count)

    print(f'#{tc}', end = ' ')
    for item in result:
        print(item, end = ' ')
    print()