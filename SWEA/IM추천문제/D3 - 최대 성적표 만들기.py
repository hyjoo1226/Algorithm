T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())    #N개의 과목 중 K개 선택
    N_lst = list(map(int, input().split())) #과목 점수 리스트

    N_lst.sort(reverse=True)    #내림차순 정렬
    sum = 0 #총합
    for i in range(K):
        sum += N_lst[i]
    print(f'#{tc} {sum}')