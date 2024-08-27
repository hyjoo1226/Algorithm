def btm_top(top, arr, token, i, j):   #btm 인덱스로 top 구하기
    # A,F / B,D / C,E 주사위 btm top
    if token == 0:  #첫 주사위
        idx = i
        btm = arr[j][i]
        token = 1
    else:   #이후 주사위
        btm = top
        idx = arr[j].index(btm)

    if idx == 0:    #btm idx로 top찾기
        top = arr[j][5]
    elif idx == 1:
        top = arr[j][3]
    elif idx == 2:
        top = arr[j][4]
    elif idx == 3:
        top = arr[j][1]
    elif idx == 4:
        top = arr[j][2]
    else:
        top = arr[j][0]

    return btm, top, token

def dice(btm, top): #btm, top 제외한 눈 중 가장 큰 수 반환
    max_num = 1
    for i in range(1, 7):
        if i != btm and i != top:
            if max_num < i:
                max_num = i
    return max_num

N = int(input())    #주사위 개수 N
arr = [[0] * 6 for _ in range(N)]
for i in range(N):  #주사위 배열 입력
    arr[i] = list(map(int, input().split()))

result = 0
top = 0
for i in range(6):  #첫 주사위 세팅
    dice_sum = 0
    token = 0   #token이 0이면 첫 주사위
    for j in range(N):
        btm, top, token = btm_top(top, arr, token, i, j)
        dice_sum += dice(btm, top)
    if result < dice_sum:
        result = dice_sum
print(result)

