T = int(input())
for tc in range(1, T + 1):
    N = int(input())    #줄 개수 N
    A_lst = []  #첫번째 전봇대 고도
    B_lst = []  #두번째 전봇대 고도
    result = 0
    for i in range(N):
        a, b = map(int, input().split())
        if i > 0: #첫 줄 아닌 경우 연산
            for j in range(len(A_lst)): #전봇대 리스트 순회
                if (a > A_lst[j] and b < B_lst[j]) or (a < A_lst[j] and b > B_lst[j]):
                    result += 1
        A_lst.append(a) #리스트에 값 추가
        B_lst.append(b)

    print(f'#{tc} {result}')