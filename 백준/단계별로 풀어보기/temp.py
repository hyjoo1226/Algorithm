N, M = map(int, input().split())
A = []
B = []
C = []

for i in range(N):
    A.append(input().split())
for i in range(N):
    B.append(input().split())

for i in range(len(A)):
    temp = []
    for j in range(len(B)):
        temp.append(int(A[i][j]) + int(B[i][j]))
    C.append(temp)


for i in C:
    for j in range(len(i)):
        if j == len(i) - 1:
            print(i[j])
        else:
            print(i[j], end=' ')
    print()