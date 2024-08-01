import sys
sys.stdin = open("input.txt", "r")

#가로체크
def is_check_width(arr, target):    #target 양 옆이 0인경우 0반환, 아니면 1만난 쪽으로 진행방향 변경 후 1 반환
    if target[1] == 0:   #인덱스 벗어나는 값 예외처리(왼쪽 끝)
        if arr[target[0]][1] == 0:
            return 0
        else:
            target[2] = 'right'
            return 1
    elif target[1] == 99:   #오른쪽 끝
        if arr[target[0]][98] == 0:
            return 0
        else:
            target[2] = 'left'
            return 1
    else:   # 양 옆 체크
        if (arr[target[0]][target[1] + 1] == 0) and (arr[target[0]][target[1] - 1] == 0):
            return 0
        else:
            if arr[target[0]][target[1] - 1] == 1:
                target[2] = 'left'
                return 1
            if arr[target[0]][target[1] + 1] == 1:
                target[2] = 'right'
                return 1

def is_check_length(arr, target):   #target 위가 0인경우 1 반환, 1인경우 0 반환
    if arr[target[0] - 1][target[1]] == 0:
        return 1
    else:
        return 0


def move(target, direction):    #target 이동
    if direction == 'up':       #위쪽으로 한칸
        target[0] -= 1
    if direction == 'left':     #왼쪽으로로 한칸
        target[1] -= 1
    if direction == 'right':    #오른쪽으로 한칸
        target[1] += 1

for test_case in range(1, 11):
    num = int(input())  #테스트케이스 번호
    arr = [list(map(int, input().split())) for _ in range(100)] #사다리 입력된 100x100 배열

    target = [99, 0, 'up']  #지정된 도착점(2값)의 인덱스 초기화(target[2]은 진행방향), target이 사다리 윗쪽으로 이동할 예정
    for k in range(100): #마지막 행 순회하며 2를 만나면 target기록
        if arr[99][k] == 2:
            target[1] = k
            break

    switch = 0
    while target[0] != 0:   #첫 행에 도달할 때까지 반복
        if switch == 0:  #switch가 0이면(위로 한칸 이동한 후 가로체크(target 양 옆이 0인지))
            move(target, 'up')
            switch = is_check_width(arr, target)
        
        if switch == 1:  #switch가 1이면(가로로 한칸 이동한 후 세로체크(target 위가 0인지))
            if switch == 1 and target[2] == 'left':
                move(target, 'left')
            if switch == 1 and target[2] == 'right':
                move(target, 'right')
            switch = is_check_length(arr, target)
    
    result = target[1]
    print(f'#{test_case} {result}')