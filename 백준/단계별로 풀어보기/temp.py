# a = list(map(int, input().split()) 입력값 정수형 리스트로 받기

dice = list(map(int, input().split()))
dice.sort()
dice.reverse()

if dice[0] == dice[1]:
    if dice[0] == dice[2]:
        prize = 10000 + dice[0] * 1000
    else:
        prize = 1000 + dice[0] * 100
else:
    if dice[1] == dice[2]:
        prize = 1000 + dice[1] * 100
    else:
        prize = dice[0] * 100

print(prize)