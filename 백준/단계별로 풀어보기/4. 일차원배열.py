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

#10813 공 바꾸기

#5597 과제 안 내신 분..?

#3052 나머지

#10811 바구니 뒤집기

#1546 평균