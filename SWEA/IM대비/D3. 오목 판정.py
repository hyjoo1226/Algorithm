T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[1] * N for _ in range(N)]   #NxN 오목판 입력
    for i in range(N):
        arr[i] = input()

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':    #내 위치에 돌이 있다면
                for k in range(4):
                    count = 1
                    for idx in range(1, 5): #전부 o면 오목
                        di = [idx, 0, idx, idx]  # 하, 우, 대각아래(오, 왼) - 오른쪽아래로 순회해나가므로
                        dj = [0, idx, idx, -idx]
                        if arr[i + di[k]][j + dj[k]] != 'o'    #o가 아니면
                            break
                        else:   #o면
                            count += 1