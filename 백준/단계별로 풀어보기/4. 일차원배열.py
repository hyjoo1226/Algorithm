#10807 개수세기
N = int(input())
A = list(map(int, input().split()))
v = int(input())
count = 0

for i in A:
    if i == v:
        count += 1
print(count)

#10871 X보다 작은 수
N, X = map(int, input().split())
A = list(map(int, input().split()))
for i in A:
    if i < X:
        print(i, end = " ")

#10818 최소, 최대
N = int(input())
A = list(map(int, input().split()))
min = A[0]
max = A[0]

for i in A:
    if i < min:
        min = i
    if i > max:
        max = i
print(min, max)

#2562 최댓값
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

#10810 공 넣기
N, M = map(int, input().split())
result = list(range(N))

for a in result:
    result[a] = 0

for i in range(M):
    i, j, k = map(int, input().split())
    for b in range(j - i + 1):
        result[b + i - 1] = k

for c in result:
    print(c, end=" ")

#10813 공 바꾸기
N, M = map(int, input().split())
box = list(range(N))

for i in range(N):
    box[i] = i + 1
for i in range(M):
    i, j = map(int, input().split())
    box[i - 1], box[j - 1] = box[j - 1], box[i - 1]

for i in box:
    print(i, end=" ")

#5597 과제 안 내신 분..?
students = list(range(30))
for i in students:
    students[i] = i + 1

for i in range(28):
    temp = int(input())
    if temp in students:
        students.remove(temp)

print(students[0])
print(students[1])

#3052 나머지
A = []

for i in range(10):
    temp = int(input()) % 42
    if temp not in A:
        A.append(temp)
print(len(A))

#10811 바구니 뒤집기
N, M = map(int, input().split())
box = []
for i in range(N):
    box.append(i + 1)
for k in range(M):
    i, j = map(int, input().split())
    sub = j - i
    if sub == 0:
        continue
    elif sub % 2 == 0:
        sub = int(sub / 2)
    else:
        sub = sub // 2 + 1
    for l in range(sub):
        box[i - 1], box[j - 1] = box[j - 1], box[i - 1]
        i += 1
        j -= 1
for i in box:
    print(i, end = " ")

#1546 평균
N = int(input())
score = list(map(int, input().split()))
score.sort()
M = score[-1]
temp = 0
for i in score:
    temp += i / M * 100
print(temp / len(score))