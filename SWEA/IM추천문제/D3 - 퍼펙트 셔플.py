T = int(input())
for tc in range(1, T + 1):
    N = int(input())    #카드 개수
    card = list(input().split())

    if N % 2 == 0:  #짝수면
        idx = N // 2
    else:   #홀수면
        idx = N // 2 + 1

    print(f'#{tc}', end = ' ')
    for i in range(N // 2): #절반 나눠서 차례대로 출력
        print(card[i], end = ' ')
        print(card[idx + i], end = ' ')
    if N % 2 == 1:  #홀수면 한개 더 출력
        print(card[idx - 1], end = ' ')
    print()