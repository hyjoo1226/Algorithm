from pprint import pprint

A = list(map(int, input().split())) #사각형 좌표 입력값
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))
arr = [[0] * 101 for _ in range(101)]   #101x101배열

for i in range(101):    #배열 순회하며 좌표겹치면 +1해준다
    for j in range(101):
        if A[0] < j <= A[2] and A[1] < i <= A[3]:
            arr[i][j] += 1
        if B[0] < j <= B[2] and B[1] < i <= B[3]:
            arr[i][j] += 1
        if C[0] < j <= C[2] and C[1] < i <= C[3]:
            arr[i][j] += 1
        if D[0] < j <= D[2] and D[1] < i <= D[3]:
            arr[i][j] += 1

num_sum = 0
for i in range(101):
    for j in range(101):
        if arr[i][j] != 0:
            num_sum += 1

print(num_sum)
