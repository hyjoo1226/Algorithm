A = list(range(9))

for i in A:
    A[i] = int(input())

max = A[0]
temp = 1
count = 1

for i in A:
    if i > max:
        max = i
        count = temp
    temp += 1
print(max)
print(count)