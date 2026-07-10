start, end = map(int, input().split())

# Please write your code here.
target = 0
for i in range(start, end + 1):
    num = 0
    for j in range(1, i + 1):
        if i % j == 0:
            num +=1
    if num == 3:
        target += 1
print(target)