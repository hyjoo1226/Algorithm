T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[1] * N for _ in range(N)]   #NxN 오목판 입력
    for i in range(N):
        arr[i] = input()

    result = 'NO'   #최종결과
    token = 0   #반복문 탈출 위한 토큰
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':    #내 위치에 돌이 있다면
                for k in range(4):
                    count = 1
                    for idx in range(1, 5): #전부 o면 오목
                        di = [idx, 0, idx, idx]  # 하, 우, 대각아래(오, 왼) - 오른쪽아래로 순회해나가므로
                        dj = [0, idx, idx, -idx]
                        if 0 <= i + di[k] < N and 0 <= j + dj[k] < N:   #인덱스 범위 내에서
                            if arr[i + di[k]][j + dj[k]] != 'o':   #o가 아니면
                                break
                            else:   #o면
                                count += 1
                    if count == 5:  #오목완성
                        result = 'YES'
                        token = 1
                        break
                if token == 1:
                    break
            if token == 1:
                break

    print(f'#{tc} {result}')