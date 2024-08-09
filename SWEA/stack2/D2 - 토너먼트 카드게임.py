# 깊이 들어갈수록 숫자를 빼고, 뺀 횟수를 구하는 함수 생성
def check_cal(remian, N, turn=0, num=13):
    # CASE 1 : 더한 횟수가 N번 만큼이며, 남은 수가 0인 경우 -> cnt + 1
    if turn == N and remian == 0:
        global cnt; cnt += 1

    # CASE 2 : 더한 횟수( 집합 갯수 )가 N 보다 작으며, 뺀 값이 아직 양수인 경우 -> 계속 숫자 빼주기 실행
    elif turn < N and remian > 0 and num:  # 현재 숫자보다 하나 작은 수부터 0 까지 함수 실행하며 순회하며 값을 빼기
        for n in range(num - 1, 0, -1): check_cal(remian - n, N, turn + 1, n)

    # CASE 3 : 남은 수가 음수인 경우 -> 자연스럽게 아무동작 X


## 실행 ##
for t in range(int(input())):
    # 변수 입력 받기
    N, K = map(int, input().split())

    # 필요 변수 선언 및 함수 실행
    cnt = 0
    check_cal(K, N)

    print(f"#{t + 1} {cnt}")