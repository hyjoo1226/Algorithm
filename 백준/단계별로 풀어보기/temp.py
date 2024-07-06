N = int(input())
score = list(map(int, input().split()))
score.sort()
M = score[-1]
temp = 0
for i in score:
    temp += i / M * 100
print(temp / len(score))