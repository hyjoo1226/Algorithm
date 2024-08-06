T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())    #회문의 길이 M
    arr = [[0] * N for _ in range(N)]   #NxN행렬 초기화 후 입력값 받기
    for i in range(N):
        temp = input()
        for j in range(N):
            arr[i][j] = temp[j]

    result = []
    j_index = N - M
    if j_index > N // 2 - 1:
        j_index = N // 2 - 1

    for i in range(N):  #가로 회문 찾기
        token = 0   #break위한 변수

        for j in range(N - M + 1):
            check = 1   #회문이면 1, 아니면 0인 변수

            if arr[i][j] == arr[i][j + M - 1]:  #M길이 첫 값과 끝 값이 같으면
                for k in range(M // 2 - 1): #회문인지 검사 후 아니면 0
                    if arr[i][j + k] != arr[i][j + M - 1 - k]:
                        check = 0

                if check == 1:
                    result = arr[i][j : j + M]  #회문값 result에 넣기
                    token = 1
                    break

        if token == 1:
            break

    for i in range(N):  #세로 회문 찾기
        token = 0
        for j in range(N - M + 1):
            check = 1
            if arr[j][i] == arr[j + M - 1][i]:
                for k in range(M // 2 - 1):
                    if arr[j + k][i] != arr[j + M - 1 - k][i]:
                        check = 0
                if check == 1:
                    for j in range(M):
                        result.append(arr[j][i])
                    token = 1
                    break
        if token == 1:
            break

    print(f'#{tc}', end = ' ')
    for item in result:
        print(item, end = '')
    print()