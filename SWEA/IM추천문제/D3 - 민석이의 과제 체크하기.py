T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())    #수강생의 수 N, 과제제출 수 K
    K_lst = list(map(int, input().split())) #과제제출사람번호

    N_lst = []
    for i in range(1, N + 1):
        if i not in K_lst:
            N_lst.append(i)

    print(f'#{tc}', *N_lst)