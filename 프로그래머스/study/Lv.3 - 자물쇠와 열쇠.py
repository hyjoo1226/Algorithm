def solution(key, lock):
    answer = True
    N = len(lock[0]) #자물쇠 NxN
    M = len(key[0])    #열쇠 MxM
    lock_empty = 0   #자물쇠 홈 수
    lock_dict = {}   #자물쇠 홈 좌표
    key_full = 0    #열쇠 돌기 수
    key_dict1 = {}   #열쇠 돌기 좌표
    key_dict2 = {}
    key_dict3 = {}
    key_dict4 = {}
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                lock_empty += 1
                lock_dict[(i, j)] = 1
    for i in range(M):
        for j in range(M):
            if key_full[i][j] == 1:
                key_full += 1
                key_dict1[(i, j)] = 1 #시계방향 회전하며 추가
                key_dict2[j, M - i] = 1
                key_dict3[M - i, M - j] = 1
                key_dict4[M - j, i] = 1

    if lock_empty == 0:
        return answer
    if lock_empty == 1 and key_full > 0:    #자물쇠 홈 0이나 1개인 경우
        return answer

    if lock_empty > key_full:   #자물쇠 홈 수가 더 많다면 false
        answer = False
        return answer

    if lock_empty == key_full: #홈 수와 돌기 수가 같다면 단순 비교
        if lock_dict == key_dict1:
            return answer
        if lock_dict == key_dict2:
            return answer
        if lock_dict == key_dict3:
            return answer
        if lock_dict == key_dict4:
            return answer
        answer = False  #수가 같은데 맞는 짝이 없다면 false
        return answer
    else:   #홈 수보다 돌기 수가 많다면
        backup_lock = lock_dict
        arr = [[-1] * (N + 2 * (M - 1)) for _ in range(N + 2 * (M - 1))]    #패딩 넣은 자물쇠 배열
        for i in range(N + 2 * (M - 1)):
            for j in range(N + 2 * (M - 1)):
                if i >= N + M - 1 and i <= N + N + M - 1 and j >= N + M - 1 and j <= N + N + M - 1:
                    arr[i][j] = lock[i - (N + M - 1)][j - (N + M - 1)]

        di = [1, -1, 0, 0]  #델타좌표
        dj = [0, 0, 1, -1]
        for i in range(N + 2 * (M - 1)):
            for j in range(N + 2 * (M - 1)):
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if ni >= 0 and ni < N + 2 * (M - 1) and nj >= 0 and nj < N + 2 * (M - 1):   #인덱스 범위 내 델타탐색
                        for (x, y) in key_dict1.keys():
                            if ni >= 0 and ni < N + 2 * (M - 1) and nj >= 0 and nj < N + 2 * (M - 1):
                                pass
        return answer


