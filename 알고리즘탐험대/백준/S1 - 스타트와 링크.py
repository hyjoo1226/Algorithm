from itertools import combinations

N = int(input())    # N명
arr = [list(map(int, input().split())) for _ in range(N)]   # 배열 정보
result = 100000000

# 두 팀으로 나누는 모든 조합
players = set(range(1, N + 1))  # 모든 선수 숫자
for team1 in combinations(players, N // 2):
    team1 = set(team1)
    team2 = players - team1

    energe1 = 0  # 1팀 총 능력치
    energe2 = 0  # 2팀 총 능력치
    for i in team1:
        for j in team1:
            energe1 += arr[i - 1][j - 1]
    for i in team2:
        for j in team2:
            energe2 += arr[i - 1][j - 1]

    result = min(result, abs(energe1 - energe2))    # 최솟값으로 갱신

print(result)
