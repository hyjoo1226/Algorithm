#리스트를 만들고 내림차순 정렬한 뒤 단조 판단했는데 시간이 아슬아슬함(append로 리스트 만들었을 때는 초과함)
#리스트를 만들고 정렬하는 과정 없이 각 곱한 숫자에 바로바로 단조판별을 한 경우가 훨씬 시간이 단축됐었음

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    N_lst = list(map(int, input().split())) #주어진 수 리스트
    dan_lst = [0] * (N * (N - 1) // 2)   #단조 증가하는 수인지 판별할 리스트
    top = -1

    for i in range(N - 1):
        for j in range(i + 1, N):
            top += 1
            dan_lst[top] = N_lst[i] * N_lst[j]

    dan_lst.sort(reverse=True)  #내림차순 정렬
    
    for i in range(len(dan_lst)):   #숫자 문자열로 변환
        dan_lst[i] = str(dan_lst[i])

    result = -1
    for i in range(len(dan_lst)):
        token = 0   #단조 판단할 토큰
        for j in range(len(dan_lst[i]) - 1):
            if dan_lst[i][j] > dan_lst[i][j + 1]:   #단조 증가하는 수가 아니면
                token = 1
                break
        if token == 0:  #단조 증가하는 수면
            result = dan_lst[i]
            break

    print(f'#{tc} {result}')