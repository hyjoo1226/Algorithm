N = int(input())
y = 0

for i in range(1, N + 1):
    if (i % 100 == 0) and (i % 400 != 0):
        continue
    if i % 4 == 0:
        y += 1

print(y)