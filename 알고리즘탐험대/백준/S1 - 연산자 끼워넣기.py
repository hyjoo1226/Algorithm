N = int(input())    # 수의 개수 N
N_list = list(map(int, input().split()))    # 숫자 리스트
four = list(map(int, input().split()))  # 사칙연산 개수 - 더하기, 빼기, 곱하기, 나누기 순서
num_max = -1000000001    # 최댓값
num_min = 1000000001   # 최솟값

def cal(a, b, four):    # 사칙연산
    if four == 0:
        return a + b
    elif four == 1:
        return a - b
    elif four == 2:
        return a * b
    else:
        if a < 0:   # 음수처리
            return -(-a // b)
        return a // b

def rec(level, num): # 재귀
    global num_max, num_min
    if level == N:  # 종료 조건 도달 시 최댓값, 최솟값 갱신
        num_max = max(num_max, num)
        num_min = min(num_min, num)
        return

    for i in range(4):
        if four[i] != 0:    # 해당 연산자 남아있으면
            four[i] -= 1    # 연산자 사용
            rec(level + 1, cal(num, N_list[level], i))    # 연산값으로 다시 재귀
            four[i] += 1    # 연산자 복구

rec(1, N_list[0])   # 재귀 시작
print(num_max)
print(num_min)